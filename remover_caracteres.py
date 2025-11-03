import pandas as pd
import sys

if len(sys.argv) != 4:
    print("Uso: python remover_caracteres.py <arquivo_csv> <nome_coluna> <sequencia_remover>")
    sys.exit(1)

arquivo_csv = sys.argv[1]
nome_coluna = sys.argv[2]
sequencia = sys.argv[3]

try:
    print(f"Lendo arquivo: {arquivo_csv}")
    df = pd.read_csv(arquivo_csv)
    print(f"Arquivo lido com {len(df)} linhas")
    print(f"Colunas disponíveis: {list(df.columns)}")
    
    if nome_coluna in df.columns:
        print(f"Processando coluna: {nome_coluna}")
        valores_antes = df[nome_coluna].astype(str)
        print(f"Primeiros 5 valores antes: {valores_antes.head().tolist()}")
        
        df[nome_coluna] = valores_antes.str.replace(sequencia, '', regex=False)
        valores_depois = df[nome_coluna]
        print(f"Primeiros 5 valores depois: {valores_depois.head().tolist()}")
        
        df.to_csv(arquivo_csv, index=False)
        print(f"Sequência '{sequencia}' removida da coluna '{nome_coluna}' no arquivo '{arquivo_csv}'")
    else:
        print(f"Erro: Coluna '{nome_coluna}' não encontrada")
        
except FileNotFoundError:
    print(f"Erro: Arquivo '{arquivo_csv}' não encontrado")
except Exception as e:
    print(f"Erro: {e}")