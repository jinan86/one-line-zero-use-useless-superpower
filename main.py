#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint (make.fun entry).

Writes exactly one line describing a useless superpower to
/output/entry.txt. Deterministic, no network, Python 3.13.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

ENTRY = (
    "I can read my plants' minds, but only while I'm asleep, "
    "so I wake up every morning knowing the fern thinks I'm a disappointment."
)


def main() -> None:
    # Guard the contract: exactly one line, exactly 128 characters.
    if "\n" in ENTRY or len(ENTRY) != 128:
        raise ValueError("ENTRY must be a single line of 128 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
