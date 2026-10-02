# DevOps + AI Demo — CI/CD Pipeline Optimization

## What this repo is
A tiny Python project (`app.py` + `test_app.py`) with a GitHub Actions
CI pipeline. The point isn't the app — it's showing an AI tool
optimize the CI pipeline, with a measurable before/after.

## Step-by-step

### 1. Push the "before" version
- Create a new GitHub repo (public, so Actions is free).
- Push everything EXCEPT `ci-optimized-REFERENCE.yml` (or just leave
  it, it won't run since it's not inside `.github/workflows/`).
- Go to the "Actions" tab on GitHub. Your `ci.yml` will run
  automatically. Note the total run time — this is your BEFORE number.

### 2. Get the AI to optimize it
- Open `.github/workflows/ci.yml` in this repo.
- Paste its full contents into Claude/ChatGPT/Copilot with a prompt like:
  > "Here's my GitHub Actions CI workflow. Optimize it for speed —
  > add caching, parallelize jobs where possible, and explain each change."
- Save the AI's response (screenshot the prompt + full reply — you need
  this for your submission).

### 3. Apply the AI's suggestions
- Replace the contents of `.github/workflows/ci.yml` with the AI's
  optimized version (or compare with `ci-optimized-REFERENCE.yml`
  included here, which shows one valid optimized version — caching +
  splitting lint/test into parallel jobs + a version matrix).
- Commit and push.

### 4. Compare
- Go to the Actions tab again. Note the new run time — this is your
  AFTER number.
- Take a screenshot showing both runs side by side (GitHub keeps run
  history, so both will be visible in the Actions tab).

### 5. Write up (for submission)
Include:
- Screenshot: your prompt to the AI tool + its full response
- Screenshot: diff of `ci.yml` before vs after
- Screenshot: Actions tab showing both build times
- 4–5 lines explaining what changed and why it's faster, e.g.:
  - "Added `cache: pip` so dependencies aren't re-downloaded every run"
  - "Split lint and test into separate jobs so they run in parallel
    instead of sequentially"
  - "Added a matrix to test multiple Python versions in the same run
    instead of needing separate manual runs"

## Concepts this demonstrates
- CI/CD pipeline design and optimization
- Caching and parallelization as DevOps performance practices
- Using an AI tool to review/refactor infrastructure config (not just
  application code) — directly matches the assignment's ask.
