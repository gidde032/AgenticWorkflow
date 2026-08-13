"""Detection-logic tests for the patched eval harness.

Replays synthetic `claude -p --output-format stream-json` streams through the
real detection loop, so the two known scoring bugs stay fixed. No API calls.
"""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

HARNESS = Path(__file__).parent / "scripts" / "run_eval.py"
NAME = "my-skill-skill-abc12345"  # f"{skill_name}-skill-{unique_id}"


def _start(tool):        return {"type":"stream_event","event":{"type":"content_block_start","content_block":{"type":"tool_use","name":tool}}}
def _delta(js):          return {"type":"stream_event","event":{"type":"content_block_delta","delta":{"type":"input_json_delta","partial_json":js}}}
def _stop():             return {"type":"stream_event","event":{"type":"content_block_stop"}}
def _msg_stop():         return {"type":"stream_event","event":{"type":"message_stop"}}
def _result():           return {"type":"result"}


def detect(events):
    """Run the harness's detection loop against a canned stream via a fake `claude`."""
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        (td / ".claude").mkdir()
        stream = "\n".join(json.dumps(e) for e in events) + "\n"
        fake = td / "claude"
        fake.write_text("#!/bin/sh\ncat <<'EOF'\n" + stream + "EOF\n")
        fake.chmod(0o755)
        probe = td / "probe.py"
        probe.write_text(
            "import sys, uuid\n"
            f"sys.path.insert(0, {str(HARNESS.parent.parent)!r})\n"
            "from scripts.run_eval import run_single_query\n"
            f"uuid.uuid4 = lambda: type('U',(),{{'hex':'abc12345'+'0'*24}})()\n"
            f"print(run_single_query('q', 'my-skill', 'desc', 20, {str(td)!r}, None))\n"
        )
        env = {**os.environ, "PATH": f"{td}:{os.environ['PATH']}"}
        out = subprocess.run([sys.executable, str(probe)], capture_output=True, text=True, env=env, cwd=td)
        return out.stdout.strip().endswith("True")


class TestDetection(unittest.TestCase):
    def test_skill_invoked_first_is_detected(self):
        self.assertTrue(detect([_start("Skill"), _delta(f'{{"skill":"{NAME}"}}'), _stop(), _result()]))

    def test_preamble_tool_then_skill_is_detected(self):
        """REGRESSION: a TodoWrite/Bash preamble used to score an immediate miss."""
        self.assertTrue(detect([
            _start("TodoWrite"), _delta('{"todos":[]}'), _stop(),
            _start("Bash"), _delta('{"command":"ls"}'), _stop(),
            _start("Skill"), _delta(f'{{"skill":"{NAME}"}}'), _stop(), _result(),
        ]))

    def test_sibling_skill_name_is_not_counted(self):
        """A concurrent run's identically-described command must not count."""
        self.assertFalse(detect([
            _start("Skill"), _delta('{"skill":"my-skill-skill-99999999"}'), _stop(), _result(),
        ]))

    def test_wrong_skill_then_right_skill_is_detected(self):
        self.assertTrue(detect([
            _start("Skill"), _delta('{"skill":"other-skill-11111111"}'), _stop(), _msg_stop(),
            _start("Skill"), _delta(f'{{"skill":"{NAME}"}}'), _stop(), _result(),
        ]))

    def test_never_invoked_is_not_detected(self):
        self.assertFalse(detect([
            _start("Bash"), _delta('{"command":"ls"}'), _stop(), _msg_stop(), _result(),
        ]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
