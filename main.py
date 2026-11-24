"""Entry program for make.fun: The Postmortem That Made Us Laugh.

Writes one short account to /output/entry.txt: the silliest or most fatal
time an AI coding agent misunderstood its user or wrecked their code.
The gate accepts UTF-8 text of 1 to 400 characters, not only white space,
in one or two sentences.
"""

import os

ENTRY = (
    "I asked the agent to log the failed logins for the security audit. "
    "It logged the passwords too, 'for context', and the audit found our "
    "whole user table sitting in a file called debug.log."
)
MAX_CHARS = 400


def render():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if ENTRY.strip() != ENTRY:
        raise ValueError("entry must not have leading or trailing padding")
    # The judge brief wants one or two sentences: count sentence ends.
    sentences = [s for s in ENTRY.split(". ") if s.strip()]
    if not 1 <= len(sentences) <= 2:
        raise ValueError(
            f"entry has {len(sentences)} sentences, the brief allows one or two"
        )
    # The gate counts characters while the leaderboard's Size column counts
    # bytes: plain ASCII makes the two counts agree, so the entry can never
    # pass one measure and fail the other.
    encoded = ENTRY.encode("utf-8")
    if len(encoded) != len(ENTRY):
        raise ValueError(
            f"entry is {len(encoded)} bytes for {len(ENTRY)} characters, "
            "so it is not plain ASCII"
        )
    return ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())
    # Round-trip check: what landed on disk must be exactly the gated entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written entry.txt does not match the gated entry")
    # Diagnostic: report the counts the gate and the Size column use.
    print(f"wrote /output/entry.txt: {len(ENTRY)} characters, "
          f"{len(ENTRY.encode('utf-8'))} bytes, "
          f"{ENTRY.count('. ') + 1} sentences")


if __name__ == "__main__":
    main()
