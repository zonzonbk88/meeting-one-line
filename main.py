"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire pointless
meeting to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network, no trailing newline.
"""

import os

ENTRY = (
    "The answer is yes \u2014 it was yes in yesterday's email, "
    "and it will still be yes when this call ends in twenty-nine minutes."
)


def main() -> None:
    # Gate enforced at build time: 1-200 chars, one line, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside gate"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
