"""One-star review of Monday as if it were a restaurant.

The whole entry is a single line: a diner complains that Monday sat them
at the worst table, the waiter served a whole cold week, and the bill
charged them for the weekend too. Nothing else is needed here — the
script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The review itself: one line, 115 characters, 23 words.
# Kept short on purpose: a one-star review should be quotable in one breath.
REVIEW = (
    "One star. Monday sat me at the worst table, the waiter served "
    "a whole cold week and charged me for the weekend too."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 180
MAX_WORDS = 25


def validate(line: str) -> str:
    """Strip and sanity-check the review; raise ValueError on bad input.

    Enforces the competition gate and rubric criterion 5: 1-180 chars,
    at most 25 words, a single line, and plain text only — no hashtags,
    stage directions, or markdown.
    """
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"review must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if len(text.split()) > MAX_WORDS:
        raise ValueError(
            f"review must be at most {MAX_WORDS} words, "
            f"got {len(text.split())}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    forbidden = set("#[]*_`")
    bad = sorted(forbidden & set(text))
    if bad:
        raise ValueError(
            f"review must be plain text, found forbidden characters: {bad}"
        )
    return text


def main() -> None:
    text = validate(REVIEW)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
