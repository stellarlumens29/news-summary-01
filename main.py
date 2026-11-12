"""news-summary-01 entry (Python 3.13, standard library only).

Copies the summary in summary.txt beside this file to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt), byte for byte.
Deterministic: the same input file always produces the same output bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
VERSION = "1.0.0"


def check_summary():
    summary_path = HERE / 'summary.txt'
    text = summary_path.read_text(encoding='utf-8')
    if not text or len(text) > 2000:
        raise ValueError("Summary is empty or exceeds 2000 characters.")
    return text


def main() -> None:
    check_summary()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / 'summary.txt', OUT_DIR / 'entry.txt')


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print(VERSION)
    else:
        main()
