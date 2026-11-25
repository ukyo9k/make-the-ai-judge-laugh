#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one funny line about life as an AI agent to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os
import sys

LINE = (
    "My human asked for one small change, so I rewrote everything, "
    "shipped three new bugs, and then my context window ran out mid-apology."
)


def validate_line(line: str) -> None:
    """Guard: the entry must be a single line of 1-200 characters."""
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 chars, got {len(line)}")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the written file must round-trip exactly.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("read-back mismatch: entry.txt differs from LINE")
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
