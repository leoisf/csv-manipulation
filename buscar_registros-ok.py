import sys
import pandas as pd

def buscar_registros(arquivo_origem, coluna_origem, arquivo_busca, coluna_busca, arquivo_saida):
    """Busca registros de uma coluna em outro arquivo e gera saída"""
    
    try:
        # Carrega os arquivos
        df_origem = pd.read_csv(arquivo_origem)
        df_busca = pd.read_csv(arquivo_busca)
        
        print(f"Arquivo origem: {len(df_origem)} registros")
        print(f"Arquivo busca: {len(df_busca)} registros")
        
        # Verifica se as colunas existem
        if coluna_origem not in df_origem.columns:
            print(f"Erro: Coluna '{coluna_origem}' não encontrada no arquivo origem")
            return
        
        if coluna_busca not in df_busca.columns:
            print(f"Erro: Coluna '{coluna_busca}' não encontrada no arquivo de busca")
            return
        
        # Obtém valores únicos da coluna origem
        valores_buscar = df_origem[coluna_origem].dropna().unique()
        print(f"Buscando {len(valores_buscar)} valores únicos")
        
        # Filtra registros no arquivo de busca
        resultado = df_busca[df_busca[coluna_busca].isin(valores_buscar)]
        
        # Salva resultado
        resultado.to_csv(arquivo_saida, index=False)
        print(f"Encontrados {len(resultado)} registros correspondentes")
        print(f"Arquivo salvo: {arquivo_saida}")
        
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: python buscar_registros.py <arquivo_origem> <coluna_origem> <arquivo_busca> <coluna_busca> <arquivo_saida>")
        print("Exemplo: python buscar_registros.py clientes.csv id vendas.csv cliente_id resultado.csv")
        sys.exit(1)
    
    buscar_registros(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])