#!/usr/bin/env python3
"""Concatenate two CSV files.

Usage:
    python concat_files.py input1.csv input2.csv output.csv

Compares headers and concatenates CSV files if headers match.
"""

import argparse
import csv
from pathlib import Path


def concat_csv_files(file1: str, file2: str, output: str) -> None:
    """Concatenate CSV files after comparing headers."""
    path1 = Path(file1)
    path2 = Path(file2)
    
    # Validate input files exist
    if not path1.exists():
        raise SystemExit(f"First input file not found: {file1}")
    if not path2.exists():
        raise SystemExit(f"Second input file not found: {file2}")
    
    # Read headers from both files
    with open(file1, 'r', encoding='utf-8') as f1:
        header1 = next(csv.reader(f1))
    
    with open(file2, 'r', encoding='utf-8') as f2:
        header2 = next(csv.reader(f2))
    
    # Compare headers
    if header1 != header2:
        print(f"Headers do not match:")
        print(f"File 1: {header1}")
        print(f"File 2: {header2}")
        raise SystemExit("Cannot concatenate files with different headers")
    
    # Concatenate files
    with open(output, 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(header1)  # Write header once
        
        # Write data from first file
        with open(file1, 'r', encoding='utf-8') as f1:
            reader = csv.reader(f1)
            next(reader)  # Skip header
            writer.writerows(reader)
        
        # Write data from second file
        with open(file2, 'r', encoding='utf-8') as f2:
            reader = csv.reader(f2)
            next(reader)  # Skip header
            writer.writerows(reader)
    
    print(f"Successfully concatenated {file1} and {file2} to {output}")


def main():
    parser = argparse.ArgumentParser(
        description="Concatenate two CSV files with matching headers"
    )
    parser.add_argument("file1", help="First CSV file")
    parser.add_argument("file2", help="Second CSV file") 
    parser.add_argument("output", help="Output CSV file path")
    args = parser.parse_args()

    concat_csv_files(args.file1, args.file2, args.output)


if __name__ == "__main__":
    main()