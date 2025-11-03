import pandas as pd
import sys

if len(sys.argv) != 4:
    print("Uso: python adicionar_coluna.py <arquivo_csv> <nome_coluna> <valor>")
    sys.exit(1)

arquivo_csv = sys.argv[1]
nome_coluna = sys.argv[2]
valor = sys.argv[3]

try:
    df = pd.read_csv(arquivo_csv)
    df[nome_coluna] = valor
    df.to_csv(arquivo_csv, index=False)
    print(f"Coluna '{nome_coluna}' adicionada com valor '{valor}' ao arquivo '{arquivo_csv}'")
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado")
except Exception as e:
    print(f"Erro: {e}")