"""
Called from the GitHub Actions workflow. Sends the current diff to
Claude and prints back a code review. If running on a pull request,
the workflow also posts this output as a PR comment.
"""

import os
import subprocess
import urllib.request
import json

API_KEY = os.environ["ANTHROPIC_API_KEY"]
API_URL = "https://api.anthropic.com/v1/messages"


def get_diff():
    # Diff between this push and the previous commit on the branch.
    # On the very first commit there's nothing to diff against, so
    # fall back to showing the full file contents.
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD~1", "HEAD"],
            capture_output=True, text=True, check=True
        )
        diff = result.stdout.strip()
        if diff:
            return diff
    except subprocess.CalledProcessError:
        pass

    result = subprocess.run(
        ["git", "show", "--stat", "HEAD"],
        capture_output=True, text=True
    )
    return result.stdout


def call_claude(diff_text):
    prompt = (
        "You are reviewing a code change in a CI pipeline. Give a short, "
        "practical review: point out bugs, risks, or missed edge cases. "
        "If it looks fine, say so briefly. Keep it under 150 words.\n\n"
        f"Diff:\n{diff_text}"
    )

    body = json.dumps({
        "model": "claude-sonnet-4-6",
        "max_tokens": 500,
        "messages": [{"role": "user", "content": prompt}]
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )

    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    return data["content"][0]["text"]


def main():
    diff = get_diff()
    if not diff.strip():
        print("No changes to review.")
        return

    review = call_claude(diff)

    print("=" * 60)
    print("AI CODE REVIEW")
    print("=" * 60)
    print(review)

    # Write to a file so the workflow can post it as a PR comment
    with open("ai_review_output.txt", "w") as f:
        f.write(review)


if __name__ == "__main__":
    main()
