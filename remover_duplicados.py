import sys
import pandas as pd

def remover_duplicados(arquivo_csv, arquivo_saida=None):
    """Remove registros duplicados de um arquivo CSV"""
    
    try:
        df = pd.read_csv(arquivo_csv)
        print(f"Total de registros: {len(df)}")
        
        # Remove duplicados mantendo a primeira ocorrência
        df_limpo = df.drop_duplicates()
        duplicados_removidos = len(df) - len(df_limpo)
        
        # Define arquivo de saída
        if arquivo_saida is None:
            arquivo_saida = arquivo_csv.replace('.csv', '_sem_duplicados.csv')
        
        # Salva arquivo limpo
        df_limpo.to_csv(arquivo_saida, index=False)
        
        print(f"Duplicados removidos: {duplicados_removidos}")
        print(f"Registros restantes: {len(df_limpo)}")
        print(f"Arquivo salvo: {arquivo_saida}")
        
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: python remover_duplicados.py <arquivo.csv> [arquivo_saida.csv]")
        print("Se não especificar saída, será criado arquivo_sem_duplicados.csv")
        sys.exit(1)
    
    arquivo_saida = sys.argv[2] if len(sys.argv) == 3 else None
    remover_duplicados(sys.argv[1], arquivo_saida)