def gerar_lista():
    lista = []
    try:
        with open("frutas.txt", "r") as arq:
            for linha in arq:
                lista.append(linha.strip())
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    
def main():
    lista = []
    arquivo = 'frutas.txt'
    lista = gerar_lista(arquivo)
    print(lista)

main()