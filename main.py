"""Write the one-star Moon review to /output/entry.txt.

Pure Python standard library only. Deterministic: the same entry
is written on every run.
"""

import os

RATING = "★☆☆☆☆"
GRIEVANCE = "Billions of years in orbit and it still only shows me one side."
PUNCHLINE = "Won't turn around, won't text back. Rude."
ENTRY = " ".join([RATING, GRIEVANCE, PUNCHLINE])


def validate(text):
    """Check the entry is a single non-blank line of 1-120 characters."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 120:
        raise ValueError("entry must be 1-120 characters, got %d" % len(text))
    return text


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
