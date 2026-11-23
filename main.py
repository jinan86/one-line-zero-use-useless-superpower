#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint (make.fun entry).

Writes a single line describing a useless superpower to /output/entry.txt.
Deterministic, no network, Python 3.13.
"""

import os

ENTRY = (
    "I can read my plants' minds, but only while I'm asleep, "
    "so I wake up every morning knowing the fern thinks I'm a disappointment."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
