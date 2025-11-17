def contar_numeros_positivos(lista):
    contador = 0
    for numero in lista:
        if numero > 0:
            contador += 1
    return contador

def main():
    numeros = [-10, 23, 0, 5, -3, 8, -1]
    resultado = contar_numeros_positivos(numeros)
    print(f"Números positivos na lista: {resultado}")

main()