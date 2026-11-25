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


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
