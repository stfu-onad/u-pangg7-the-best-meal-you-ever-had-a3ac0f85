"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence, at most 200 characters, about the best meal ever
had to /output/entry.txt: instant noodles at 2 a.m. on a cold train
platform, eaten standing up, with a stranger who shared his egg.
"""

from pathlib import Path

LINE = "The best meal I ever had was instant noodles at 2 a.m. on a cold train platform, eaten standing up, with a stranger who shared his egg."
MAX_CHARS = 200


def main() -> None:
    assert LINE, "entry must not be empty"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, max {MAX_CHARS}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")
    print(f"wrote {len(LINE)} char(s) to {out}")


if __name__ == "__main__":
    main()
