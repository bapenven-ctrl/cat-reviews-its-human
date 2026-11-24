#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one line — a one-star review written by a house cat about its
human — to /output/entry.txt. Deterministic, no network, no dependencies.
"""

import os

TEXT = (
    "One star. My food bowl was empty for four entire minutes. "
    "I have eaten the houseplant, the curtains, and his left shoe. "
    "In that order."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
