def remover_repetidos(lista_numeros):
    lista_unicos = set(lista_numeros)
    return(lista_unicos)

def main():
    lista_numeros = [3,3,1,2,2,4,5,5,5,6]
    resultado = remover_repetidos(lista_numeros)
    for i in resultado:
        print(i, end = ' ')
        print()

main()