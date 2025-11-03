import os
import sys
import pandas as pd
from pathlib import Path

def concatenar_csvs(pasta_entrada, arquivo_saida):
    """Concatena todos os arquivos CSV de uma pasta em um único arquivo"""
    
    pasta = Path(pasta_entrada)
    if not pasta.exists():
        print(f"Erro: Pasta '{pasta_entrada}' não encontrada")
        return
    
    # Busca todos os arquivos CSV na pasta
    arquivos_csv = list(pasta.glob("*.csv"))
    
    if not arquivos_csv:
        print(f"Nenhum arquivo CSV encontrado na pasta '{pasta_entrada}'")
        return
    
    print(f"Encontrados {len(arquivos_csv)} arquivos CSV")
    
    dataframes = []
    
    # Lê cada arquivo CSV
    for arquivo in arquivos_csv:
        try:
            df = pd.read_csv(arquivo)
            dataframes.append(df)
            print(f"Processado: {arquivo.name} ({len(df)} registros)")
        except Exception as e:
            print(f"Erro ao processar {arquivo.name}: {e}")
    
    if not dataframes:
        print("Nenhum arquivo foi processado com sucesso")
        return
    
    # Concatena todos os DataFrames
    df_final = pd.concat(dataframes, ignore_index=True)
    
    # Salva o arquivo final
    df_final.to_csv(arquivo_saida, index=False)
    print(f"Arquivo concatenado salvo: {arquivo_saida} ({len(df_final)} registros totais)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python concatenar_csv.py <pasta_entrada> <arquivo_saida>")
        print("Exemplo: python concatenar_csv.py ./dados resultado.csv")
        sys.exit(1)
    
    pasta_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2]
    
    concatenar_csvs(pasta_entrada, arquivo_saida)