# deployment-gate-repair

Intentionally broken DevOps Foundation Module 3 starter. Only documented faults/draft gaps require repair. Existing application/test is correct.

## Setup

Fork public repository and clone YOUR fork. Python 3.10+ and Git required; no packages, cloud account, Docker, Kubernetes cluster, credentials or paid services.

```bash
git clone https://github.com/YOUR-USERNAME/deployment-gate-repair.git
cd deployment-gate-repair
git switch -c fix/module3
python3 -m unittest -v
python3 check.py all
```

Initial app test passes; initial static contract check fails by design. Capture original failures before editing. Commands run from repository root. No inherited workflow runs required. Setup is outside assessment; report unrelated environment failures.

## Allowed edits

.github/workflows/release.yml, approval-review.md. Keep checker, application, tests and fixtures unchanged. No bypasses, removed checks or fabricated evidence.

## Required controls

Production must need `validate` and use `${{ success() && github.ref == 'refs/heads/main' }}`. Production environment must be `production`; job permissions must be `contents: read`; RELEASE_TOKEN must reference `${{ secrets.RELEASE_TOKEN }}`. Preserve top-level permissions, validation, safe echo command and manual trigger. Workflow is JSON-formatted YAML, valid in GitHub Actions; retain format for this assessment.

Task 1 changes two workflow fields and writes the pipeline risk/fix line. Task 2 changes environment, job permissions and secret reference (three fields). Task 3 completes the remaining three review lines: required reviewer plus self-review control configured separately, production environment secret scope, and honest production decision with missing evidence.

An environment name alone does not require approval. Reviewers, self-review prevention and deployment-branch restrictions must be set separately in GitHub settings. Do not create a real token or configure live production. Static checks cannot prove reviewer enforcement, secret availability or runtime deployment. Production approval has NOT been configured or tested in this exercise. Correct final decision remains NO-GO until required real controls are verified.

## Evidence

Follow assessment's three tasks. Submit one PDF with real screenshots, original failure, corrected diff, passing static checks and requested reasoning. Grade only the three tasks and requested evidence; repository/fork URLs, branch names and submission commit metadata are not required or graded. At least one screenshot per task. Written reports require manual grading. No PR or video. Do not run production workflows or expose secrets. Static PASS proves only exercise contract.
