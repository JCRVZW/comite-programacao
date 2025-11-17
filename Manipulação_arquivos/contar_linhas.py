def contar_linhas():
    try:
        with open('frutas.txt') as arquivo:
            return len(arquivo.readlines())
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def main():
    qtd_linhas = contar_linhas()
    print(f'Quantidade de linhas: {qtd_linhas} linhas!')

    main()