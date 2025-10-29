import pandas as pd

def verificar_registros_quebrados(nome_arquivo):
    try:
        # Tentar ler CSV com pandas para detectar problemas estruturais
        df = pd.read_csv(nome_arquivo, encoding='utf-8', on_bad_lines='skip')
        
        # Contar linhas no arquivo original
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            total_linhas_arquivo = sum(1 for _ in f) - 1  # -1 para excluir cabeçalho
        
        num_colunas_esperadas = len(df.columns)
        registros_lidos = len(df)
        registros_quebrados = total_linhas_arquivo - registros_lidos
        
        print(f"Colunas esperadas: {num_colunas_esperadas}")
        print(f"Total de linhas no arquivo: {total_linhas_arquivo}")
        print(f"Registros lidos com sucesso: {registros_lidos}")
        print(f"Registros quebrados/ignorados: {registros_quebrados}")
        
        if registros_quebrados > 0:
            print("\nArquivo contém registros com caracteres que quebram a estrutura CSV")
        
    except pd.errors.ParserError as e:
        print(f"Erro crítico ao processar CSV: {e}")
        print("Arquivo severamente corrompido")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    verificar_registros_quebrados('casos_2025-05.csv')