#!/usr/bin/env python3

import json
import os

from openai import OpenAI


def extract_action_items(meeting_notes):
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
Analyze the following meeting notes and extract all actionable tasks.

For each task, return:
- task
- owner
- deadline
- priority

If a field is not mentioned, use null.

Return valid JSON only in this format:

{{
  "action_items": [
    {{
      "task": "...",
      "owner": "...",
      "deadline": "...",
      "priority": "high|medium|low"
    }}
  ]
}}

Meeting notes:
{meeting_notes}
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text


def main():
    print("=== AI Meeting Action Extractor ===")
    print("Paste your meeting notes below.")
    print("Enter END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    notes = "\n".join(lines)

    if not notes.strip():
        print("No meeting notes provided.")
        return

    result = extract_action_items(notes)

    print("\n=== Action Items ===")

    try:
        data = json.loads(result)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print(result)


if __name__ == "__main__":
    main()
