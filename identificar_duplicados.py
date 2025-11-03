import sys
import pandas as pd

def identificar_duplicados(arquivo_csv):
    """Identifica e mostra registros duplicados em um arquivo CSV"""
    
    try:
        df = pd.read_csv(arquivo_csv)
        print(f"Total de registros: {len(df)}")
        
        # Identifica duplicados
        duplicados = df[df.duplicated(keep=False)]
        
        if duplicados.empty:
            print("Nenhum registro duplicado encontrado")
        else:
            print(f"\nEncontrados {len(duplicados)} registros duplicados:")
            print(f"Número de grupos de duplicatas: {len(duplicados.drop_duplicates())}")
            print("\n" + "="*50)
            print(duplicados.to_string(index=True))
            
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python identificar_duplicados.py <arquivo.csv>")
        sys.exit(1)
    
    identificar_duplicados(sys.argv[1])