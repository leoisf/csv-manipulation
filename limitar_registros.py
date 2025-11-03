import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Uso: python limitar_registros.py <arquivo_csv> <limite_registros>")
    sys.exit(1)

arquivo_csv = sys.argv[1]
limite = int(sys.argv[2])

try:
    df = pd.read_csv(arquivo_csv)
    df = df.head(limite)
    df.to_csv(arquivo_csv, index=False)
    print(f"Arquivo '{arquivo_csv}' limitado a {limite} registros")
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado")
except ValueError:
    print("Erro: Limite deve ser um valor inteiro")
except Exception as e:
    print(f"Erro: {e}")