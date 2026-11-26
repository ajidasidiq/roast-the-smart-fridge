#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) to /output/entry.txt.
"""

import os

ENTRY = "My smart fridge asks me to rate every ice cube it drops, like a needy coworker begging for five stars \u2014 mate, you're a fridge, not a freelancer."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
