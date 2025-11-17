def gera_lista(lista):
    for i in range(5):
        fruta = input("Informe uma fruta -> ")
        lista.append(fruta)
    return lista

def escrevver_frutas(lista):
    with open("frutas.txt", "w") as f:
        for fruta in lista:
            f.write(fruta + "\n")
            print('Arquivo Gerado!')

def main():
    lista = []
    lista = gera_lista(lista)
    escrevver_frutas(lista)

main()