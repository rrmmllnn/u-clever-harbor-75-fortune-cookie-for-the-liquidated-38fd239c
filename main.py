#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes one fortune cookie line, at most 20 words of plain text, for a
crypto trader who has just been liquidated, to /output/entry.txt.

The fortune is fixed and deterministic: every run writes the same bytes.
"""

import os

FORTUNE = "Your $47 of Bitcoin will return as coffee from a stranger at 3 a.m., and you will laugh together."

MAX_CHARS = 160
MAX_WORDS = 20


def main() -> None:
    words = FORTUNE.split()
    assert 1 <= len(FORTUNE) <= MAX_CHARS, "fortune must be 1-160 characters"
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    assert len(words) <= MAX_WORDS, "fortune must be at most 20 words"
    assert "\n" not in FORTUNE, "fortune must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
