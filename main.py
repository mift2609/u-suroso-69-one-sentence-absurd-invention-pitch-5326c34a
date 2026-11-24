"""One-Sentence Absurd Invention Pitch.

A single-sentence pitch for a ridiculous invention that fixes a tiny
everyday annoyance: an alarm clock that apologises for waking you up
and takes the blame for your early meeting. Deterministic, stdlib only.
"""

import os

LINE = (
    "A self-apologising alarm clock that wakes you with a sincere sorry, "
    "brews your coffee, and takes full blame for the 7 AM meeting you never wanted."
)


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 220, f"entry must be 1-220 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Re-read and verify exactly what was written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written entry does not match LINE"
    assert written.count("\n") == 1, "entry must be exactly one line"
    assert 1 <= len(written.strip()) <= 220, "entry must be 1-220 chars"
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
