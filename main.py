"""One Word From Your Ex.

Writes exactly one word -- the word an ex would use to describe the
entrant -- to /output/entry.txt. The word is a fixed, deliberate choice:
a flat, painfully honest verdict that is funny because the entrant is
admitting it. No input is read, no randomness, no time, no network, so
every run produces byte-identical output.
"""

import os

WORD = "Underwhelming"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
