#!/usr/bin/env python3
"""Concatenate all CSV files in a folder.

Usage:
    python concat_pasta.py pasta_csv output.csv

Compares headers and concatenates all CSV files in folder if headers match.
"""

import argparse
import csv
from pathlib import Path


def concat_all_csv_files(pasta: str, output: str) -> None:
    """Concatenate all CSV files in folder after comparing headers."""
    pasta_path = Path(pasta)
    
    if not pasta_path.exists():
        raise SystemExit(f"Folder not found: {pasta}")
    
    # Find all CSV files
    csv_files = list(pasta_path.glob("*.csv"))
    
    if not csv_files:
        raise SystemExit(f"No CSV files found in: {pasta}")
    
    print(f"Found {len(csv_files)} CSV files")
    
    # Read header from first file
    with open(csv_files[0], 'r', encoding='utf-8') as f:
        header_reference = next(csv.reader(f))
    
    # Validate all files have same header
    for csv_file in csv_files[1:]:
        with open(csv_file, 'r', encoding='utf-8') as f:
            header = next(csv.reader(f))
            if header != header_reference:
                print(f"Header mismatch in file: {csv_file}")
                print(f"Expected: {header_reference}")
                print(f"Found: {header}")
                raise SystemExit("Cannot concatenate files with different headers")
    
    # Concatenate all files
    with open(output, 'w', encoding='utf-8', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(header_reference)  # Write header once
        
        total_registros = 0
        for csv_file in csv_files:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                registros = list(reader)
                registros_count = len(registros)
                total_registros += registros_count
                print(f"Processing: {csv_file.name} - {registros_count} registros")
                writer.writerows(registros)
    
    print(f"Successfully concatenated {len(csv_files)} files to {output}")
    print(f"Total de registros: {total_registros}")


def main():
    parser = argparse.ArgumentParser(
        description="Concatenate all CSV files in a folder"
    )
    parser.add_argument("pasta", help="Folder containing CSV files")
    parser.add_argument("output", help="Output CSV file path")
    args = parser.parse_args()

    concat_all_csv_files(args.pasta, args.output)


if __name__ == "__main__":
    main()