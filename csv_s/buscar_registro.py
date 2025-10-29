#!/usr/bin/env python3
"""Search for a record in all CSV files in a folder using pandas.

Usage:
    python buscar_registro.py pasta_csv campo_busca valor_busca

Searches for a specific value in a field across all CSV files in folder.
"""

import argparse
import pandas as pd
from pathlib import Path


def buscar_registro(pasta: str, campo_busca: str, valor_busca: str) -> None:
    """Search for record in all CSV files in folder using pandas."""
    pasta_path = Path(pasta)
    
    if not pasta_path.exists():
        raise SystemExit(f"Folder not found: {pasta}")
    
    # Find all CSV files
    csv_files = list(pasta_path.glob("*.csv"))
    
    if not csv_files:
        raise SystemExit(f"No CSV files found in: {pasta}")
    
    print(f"Searching in {len(csv_files)} CSV files")
    print(f"Campo: {campo_busca} | Valor: {valor_busca}")
    print("-" * 50)
    
    registros_encontrados = 0
    
    for csv_file in csv_files:
        try:
            df = pd.read_csv(csv_file, encoding='utf-8')

           # print(df)
            
            if campo_busca not in df.columns:
                print(f"Campo '{campo_busca}' não encontrado em {csv_file.name}")
                continue
            
            # Buscar registros que correspondem ao valor
            matches = df[df[campo_busca].astype(str) == str(valor_busca)]
            
            if not matches.empty:
                for index, row in matches.iterrows():
                   # print(row)
                    registros_encontrados += 1
                    print(f"\nArquivo: {csv_file.name} | Linha: {index + 2}")  # +2 porque pandas index começa em 0 e há header
                    print("Registro encontrado:")
                    for col in df.columns:
                        print(f"  {col}: {row[col]}")
            
        except Exception as e:
            print(f"Erro ao processar {csv_file.name}: {e}")
    
    print(f"\n{'-' * 50}")
    print(f"Total de registros encontrados: {registros_encontrados}")


def main():
    parser = argparse.ArgumentParser(
        description="Search for a record in all CSV files in a folder"
    )
    parser.add_argument("pasta", help="Folder containing CSV files")
    parser.add_argument("campo_busca", help="Field name to search in")
    parser.add_argument("valor_busca", help="Value to search for")
    args = parser.parse_args()

    buscar_registro(args.pasta, args.campo_busca, args.valor_busca)


if __name__ == "__main__":
    main()