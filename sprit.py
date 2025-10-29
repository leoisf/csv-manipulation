#!/usr/bin/env python3
"""
Sort a CSV by a date/day column.

Usage:
    python sort_by_day.py input.csv --column day --output sorted.csv --format 
"""

import csv
import argparse
import io
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

DEFAULT_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y"]

def parse_date(s: str, formats: List[str]) -> Optional[datetime]:
        if s is None:
                return None
        s = s.strip()
        if s == "":
                return None
        for fmt in formats:
                try:
                        return datetime.strptime(s, fmt)
                except Exception:
                        continue
        # try ISO fallback
        try:
                return datetime.fromisoformat(s)
        except Exception:
                return None

def main():
        p = argparse.ArgumentParser(description="Sort CSV by a day/date column")
        # `input` is optional when using `-S/--string` to pass CSV content directly
        p.add_argument("input", nargs="?", help="input CSV file path (omit when using -S/--string)")
        p.add_argument("-o", "--output", help="output CSV file path (defaults to input.sorted.csv)")
        p.add_argument("-c", "--column", default="day", help="column name (default: 'day')")
        p.add_argument("-f", "--format", action="append", help="date format (can repeat). If omitted, tries common formats.")
        p.add_argument("-S", "--string", action="append", help="CSV input as string (can repeat). If provided, these strings are concatenated with newlines and used as input instead of a file")
        p.add_argument("--no-header", action="store_true", help="treat file as headerless (will sort by column index 0-based)")
        args = p.parse_args()

        # Validate inputs: either a file path or at least one --string must be provided
        if not args.input and not args.string:
                raise SystemExit("Provide an input file path or at least one -S/--string with CSV content")

        formats = args.format if args.format else DEFAULT_FORMATS

        # Read rows either from provided strings or from file
        if args.string:
                # join multiple -S arguments with newlines to form a CSV content
                csv_text = "\n".join(args.string)
                f = io.StringIO(csv_text)
                reader = csv.reader(f)
                rows = list(reader)
        else:
                inp = Path(args.input)
                if not inp.exists():
                        raise SystemExit(f"Input file not found: {inp}")
                with inp.open(newline="", encoding="utf-8") as f:
                        reader = csv.reader(f)
                        rows = list(reader)

        if not rows:
                raise SystemExit("Empty CSV")

        if args.no_header:
                header = None
                data = rows
                col_index = int(args.column) if args.column.isdigit() else 0
        else:
                header = rows[0]
                data = rows[1:]
                if args.column.isdigit():
                        col_index = int(args.column)
                else:
                        try:
                                col_index = header.index(args.column)
                        except ValueError:
                                raise SystemExit(f"Column '{args.column}' not found in header: {header}")

        # pair rows with parsed date for sorting
        def key_for_row(row):
                val = row[col_index] if col_index < len(row) else ""
                dt = parse_date(val, formats)
                # fallback: put unparsable dates at end
                return (dt is None, dt or datetime.min)

        data.sort(key=key_for_row)

        # Write output: if --output provided write to file, otherwise (when using --string)
        # print to stdout so the caller can capture it.
        if args.output:
                out = Path(args.output)
                with out.open("w", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        if header:
                                writer.writerow(header)
                        writer.writerows(data)
                print(f"Wrote sorted CSV to: {out}")
        else:
                # Default: print to stdout
                writer = csv.writer(sys.stdout)
                if header:
                        writer.writerow(header)
                writer.writerows(data)

if __name__ == "__main__":
        main()
        