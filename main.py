"""The Robot Vacuum's Funniest Excuse - make.fun entry.

Writes one line (at most 120 characters) to /output/entry.txt:
the excuse a robot vacuum gives for missing a spot.
"""

import os

LINE = (
    "I didn't miss it. I circled it three times, lost my nerve, "
    "and went back to my dock to process my feelings."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line must be 1-120 chars, got {len(text)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
