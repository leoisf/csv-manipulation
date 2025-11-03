import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Uso: python remover_linhas.py <arquivo_csv> <numero_linhas>")
    sys.exit(1)

arquivo_csv = sys.argv[1]
num_linhas = int(sys.argv[2])

try:
    df = pd.read_csv(arquivo_csv)
    df = df.iloc[num_linhas:]
    df.to_csv(arquivo_csv, index=False)
    print(f"Removidas {num_linhas} linhas do início do arquivo '{arquivo_csv}'")
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado")
except ValueError:
    print("Erro: Número de linhas deve ser um valor inteiro")
except Exception as e:
    print(f"Erro: {e}")