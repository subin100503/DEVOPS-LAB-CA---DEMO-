# Integrating AI Directly Into the CI/CD Pipeline

This adds a real AI step INSIDE your GitHub Actions pipeline — it
automatically reviews every code change and comments on it. This is
different from just pasting code into Claude manually; the AI is now
part of the automated workflow itself.

## What it does
1. Your code pushes → tests run (existing pipeline)
2. If tests pass → a new step runs that sends the diff to Claude
3. Claude reviews the change and writes feedback
4. If it's a Pull Request, the review is posted as an automatic comment

## Setup steps

### 1. Get an Anthropic API key
- Go to https://console.anthropic.com
- Sign up / log in
- Go to "API Keys" → "Create Key"
- Copy the key (starts with `sk-ant-...`) — you won't see it again, so save it somewhere safe for now

### 2. Add it as a GitHub secret (never put the key directly in your code)
1. Go to your repo on GitHub
2. Click **Settings** (top right of repo) → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `ANTHROPIC_API_KEY`
5. Value: paste your key
6. Click **Add secret**

### 3. Push the new files
The zip includes:
- `scripts/ai_review.py` — the script that calls Claude
- `.github/workflows/ci-with-ai-review.yml` — the new workflow

In your terminal (same repo folder as before):
```
git add .
git commit -m "Integrate AI code review into CI pipeline"
git push
```

### 4. Trigger it properly (to see the PR comment feature)
The AI comment step only fires on Pull Requests, so:
1. Make a small change to `app.py` (e.g. add a new function)
2. Create a new branch:
   ```
   git checkout -b test-ai-review
   git add .
   git commit -m "Test change for AI review"
   git push origin test-ai-review
   ```
3. On GitHub, click **Compare & pull request**, then **Create pull request**
4. Wait ~30-60 seconds — the AI will automatically comment on your PR with a code review

### 5. Screenshot for your submission
- The GitHub secret setup page (blur/hide the actual key)
- The Actions tab showing the `ai-review` job running
- The PR with the AI's comment visible
- The workflow YAML + script code

## Why this satisfies "integrate AI into workflow"
- The AI isn't a separate manual step you do yourself — it's triggered
  automatically by the pipeline, on every push/PR
- It uses the actual Claude API (not just chatting with an AI tool)
- It demonstrates AI optimizing a real DevOps process: automated code
  review, which normally needs a human reviewer
