import csv
import argparse

def ordena_csv(nomeArquivo: str, colunaOrdenacao: str, saidaArquivo: str) -> None:
    #coluna_ordenacao = 'create_date'
    registros = []
    #nome_arquivo = 'comentarios_ordenados.csv'
    cabecalho = None

    with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for i, linha in enumerate(leitor_csv):
            if i == 0:
                cabecalho = linha
                try:
                    colunaOrd = cabecalho.index(colunaOrdenacao)
                    print(f"Ordenando pela coluna {colunaOrd}: {colunaOrdenacao}")
                except ValueError:
                    print(f"Campo '{colunaOrdenacao}' não encontrado no cabeçalho.")
                    print(f"Campos disponíveis: {cabecalho}")
                    exit(1)
            else:
                registros.append(linha)
                #print(linha)

    registros = [r for r in registros if any(campo.strip() for campo in r)]
    registros.sort(key=lambda x: x[colunaOrd] if len(x) > colunaOrd else '')

    with open(saidaArquivo, 'w', encoding='utf-8', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(registros)

    print(f"\n--- Lista ordenada por {cabecalho[colunaOrd]} ---")
    """ for registro in registros:
        print(registro) """


def main():
    parser = argparse.ArgumentParser(
        description="Concatenate two files into one output file"
    )
    parser.add_argument("nomeArquivo", help="File for ordenation")
    parser.add_argument("colunaOrdenacao", help="Column name for ordenation") 
    parser.add_argument("saidaArquivo", help="Output output ordened file path")
    args = parser.parse_args()

    ordena_csv(args.nomeArquivo, args.colunaOrdenacao, args.saidaArquivo)

if __name__ == "__main__":
    main()