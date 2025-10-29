import csv

def processar_csv(nome_arquivo, coluna_ordenacao):
    registros = []
    cabecalho = None
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for i, linha in enumerate(leitor_csv):
            if i == 0:
                cabecalho = linha
                try:
                    indice_coluna = cabecalho.index(coluna_ordenacao)
                except ValueError:
                    indice_coluna = 2
                print(linha)
            else:
                registros.append(linha)
    
    registros = [r for r in registros if any(campo.strip() for campo in r)]
    registros.sort(key=lambda x: x[indice_coluna] if len(x) > indice_coluna else '')
    
    with open('comentarios_ordenados.csv', 'w', encoding='utf-8', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(registros)
    
    print(f"\n--- Lista ordenada por {cabecalho[indice_coluna]} ---")

if __name__ == "__main__":
    processar_csv('comentarios_ordenados.csv', 'create_date')