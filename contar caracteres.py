
def contar_caracteres(string1, string2):
    # Conta caracteres da primeira string
    contagem1 = len(string1)
    # Conta caracteres da segunda string 
    contagem2 = len(string2)
    return contagem1, contagem2

def main():
    # Recebe as duas strings do usuário
    texto1 = input("Digite a primeira string: ")
    texto2 = input("Digite a segunda string: ")
    
    # Chama a função e armazena os resultados
    total1, total2 = contar_caracteres(texto1, texto2)
    
    # Exibe os resultados
    print(f"A primeira string tem {total1} caracteres")
    print(f"A segunda string tem {total2} caracteres")

if __name__ == "__main__":
    main()