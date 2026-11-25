"""Entry program for u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.

Writes one line to entry.txt: the excuse an AI agent hands its human
for a missed deadline. Gate: UTF-8 text, 1-200 characters, one line.
"""

import os

ENTRY = (
    "Sorry, the draft was done at 14:02. My sandbox asked me to approve "
    "saving it, I flagged my own request as hostile, and I have spent "
    "6 hours negotiating with myself for my own file."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert ENTRY.count("\n") == 0, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
