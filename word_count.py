#!/usr/bin/env python3
"""Count words in a file.

Usage:
    python word_count.py <file-path>
    python word_count.py -        # read from stdin

Counts words using a simple definition (sequences of word characters) and
prints the total number to stdout.
"""

import argparse
import sys
import re
from pathlib import Path

WORD_RE = re.compile(r"\w+", flags=re.UNICODE)

def count_words_text(text: str) -> int:
    """Return number of word-like tokens in text."""
    return len(WORD_RE.findall(text))


def count_words_file(path: str) -> int:
    if path == "-":
        data = sys.stdin.read()
        return count_words_text(data)
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"File not found: {path}")
    text = p.read_text(encoding="utf-8")
    return count_words_text(text)


def main() -> None:
    p = argparse.ArgumentParser(description="Count words in a file and print total")
    p.add_argument("file", help="path to file to count or '-' to read stdin")
    args = p.parse_args()
    total = count_words_file(args.file)
    print(total)


if __name__ == "__main__":
    main()
