#!/usr/bin/env python3

import os
import subprocess

from openai import OpenAI


def get_git_diff():
    result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True,
        text=True,
        check=True,
    )

    return result.stdout


def generate_commit_message(diff):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
Analyze the following Git diff and generate a concise commit message.

Use Conventional Commits format:

<type>(<scope>): <description>

Allowed types:
- feat
- fix
- refactor
- perf
- docs
- test
- chore

Rules:
- Keep the subject under 72 characters.
- Use imperative mood.
- Do not mention implementation details unless important.
- Return only the commit message.

Git diff:
{diff}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text.strip()


def main():
    print("=== AI Git Commit Generator ===")

    diff = get_git_diff()

    if not diff.strip():
        print("No staged changes found.")
        print("Use `git add` before running this script.")
        return

    print("Analyzing staged changes...\n")

    try:
        message = generate_commit_message(diff)

        print("Suggested commit message:")
        print()
        print(message)

    except subprocess.CalledProcessError as error:
        print(f"Git command failed: {error}")

    except Exception as error:
        print(f"AI analysis failed: {error}")


if __name__ == "__main__":
    main()
