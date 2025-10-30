def pares(lista_numeros):

    lista_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
    return lista_pares

def main():
    numeros = [2,3,5,7,10,13,16,20]
    lista_final = pares(numeros)
    for numero in lista_final:
       print(numero)
main()