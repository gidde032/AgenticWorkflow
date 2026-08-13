# Repository-Owned GitHub Actions Contract

The GitHub Actions workflow is the canonical clean-environment verification
layer for pull requests. Local hooks provide earlier feedback but do not replace
the repository-owned check.

## Workflow requirements

- Trigger on pull requests targeting the protected/default branch.
- Install dependencies from the repository's declared lock or dependency files.
- Run the canonical gate from a clean checkout.
- Give the required job a stable, unique name.
- Avoid giving unrelated workflows or jobs the same required-check name.
- Keep auto-fix out of the canonical CI job.
- Add `merge_group` when the repository adopts GitHub's merge queue.
- Record the exact local-equivalent command in the operating rules.

GitHub identifies a workflow check by its job name, and required checks do not
distinguish workflow, matrix, or trigger type. Stable unique naming prevents
ambiguous required checks. See
[GitHub's rules troubleshooting documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/troubleshooting-rules).

Treat pre-commit.ci or any similar hosted auto-fix integration as optional,
and default it to disabled unless the project profile explicitly chooses it.
The repository-owned GitHub Actions job remains the canonical required
check.

## Required-check activation order

1. Add and validate the workflow locally where possible.
2. Push it on a branch and let the repository-owned Actions job complete.
3. Confirm the exact check name and producing app in the PR.
4. Only then add it as a required status check.
5. Select the repository's Actions source when it is identifiable.
6. Do not select an unrelated integration such as pre-commit.ci merely because
   it exposes a similar name.
7. Re-open a PR or push a harmless follow-up when needed to prove the rule blocks
   a failing check and permits a passing one.
8. Report configuration and observed enforcement separately.

GitHub currently requires a selectable required check to have completed
successfully in the repository during the preceding seven days. Merge queues
also require workflows to listen for `merge_group`. See
[GitHub's required-check troubleshooting guide](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).

When an expected source is selected, GitHub requires the app to have recently
submitted the check. Selecting "any source" does not authenticate one producer;
the merge box must then be inspected for the check author. See
[GitHub's ruleset reference](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).

## Ruleset truthfulness

Record separately:

```text
Ruleset verification
- Configured: <rules and target branch>
- Enforcement status: <active/disabled>
- Repository plan/visibility support: <verified result>
- Failing-check block observed: <yes/no and evidence>
- Passing-check merge path observed: <yes/no and evidence>
- Remaining limitation: <none or explicit>
```

Do not claim enforcement merely because a ruleset was saved. Availability
depends on repository visibility and plan, so verify the current repository
rather than hardcoding an assumption. GitHub documents branch/tag rulesets for
public repositories on Free plans and for public or private repositories on
Pro, Team, and Enterprise plans. Treat
[GitHub's ruleset documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
as the current authority.

---
