import csv

def verificar_registros_quebrados(nome_arquivo):
    registros_quebrados = 0
    total_registros = 0
    num_colunas_esperadas = None
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for i, linha in enumerate(leitor_csv):
            if i == 0:
                num_colunas_esperadas = len(linha)
                print(f"Colunas esperadas: {num_colunas_esperadas}")
            else:
                total_registros += 1
                if len(linha) != num_colunas_esperadas:
                    registros_quebrados += 1
                    print(f"Linha {i+1}: {len(linha)} colunas - Esperado: {num_colunas_esperadas}")
    
    print(f"\nTotal de registros: {total_registros}")
    print(f"Registros quebrados: {registros_quebrados}")
    print(f"Registros válidos: {total_registros - registros_quebrados}")

if __name__ == "__main__":
    verificar_registros_quebrados('casos_2025-05.csv')