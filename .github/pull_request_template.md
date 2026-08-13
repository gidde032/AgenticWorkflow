<!--
This repo runs its own workflow. Open PRs as drafts after the first green commit;
mark ready only after independent review. See CONTRIBUTING.md.
-->

## What & why

<!-- One or two sentences. Link the owning Issue. -->

Closes #

## Change

<!-- What changed. If a skill's behavior changed, say which routing or execution
     behavior moved, not just which lines. -->

## Evidence

<!-- This workflow changes on evidence, not theory. For code/scripts: red→green
     test output. For skills: routing/execution eval results, or the lived
     example that motivated the change. -->

- [ ] Local gates pass (`bash skills/agentic-docs-github-migration/scripts/run_fixtures.sh` if migration scripts changed)
- [ ] Affected skills stay under 500 lines and cross-references resolve
- [ ] Docs reconciled (README / CONTRIBUTING / examples) if behavior or surface changed

## Reviewer notes

<!-- Anything a contextless reviewer needs: the exact base/head, what to focus on. -->
