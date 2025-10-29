import csv

coluna_ordenacao = 'create_date'
registros = []
nome_arquivo = 'comentarios_ordenados.csv'
cabecalho = None
with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    for i, linha in enumerate(leitor_csv):
        if i == 0:
            cabecalho = linha
            nome_campo = linha[0]
            try:
                coluna_ordenacao = cabecalho.index(nome_campo)
            except ValueError:
                coluna_ordenacao = 2
            #print(linha)
        else:
            registros.append(linha)
            #print(linha)

registros = [r for r in registros if any(campo.strip() for campo in r)]
registros.sort(key=lambda x: x[coluna_ordenacao] if len(x) > coluna_ordenacao else '')

with open('comentarios_ordenados.csv', 'w', encoding='utf-8', newline='') as arquivo_saida:
    escritor_csv = csv.writer(arquivo_saida)
    escritor_csv.writerow(cabecalho)
    escritor_csv.writerows(registros)

print(f"\n--- Lista ordenada por {cabecalho[coluna_ordenacao]} ---")
""" for registro in registros:
    print(registro) """

