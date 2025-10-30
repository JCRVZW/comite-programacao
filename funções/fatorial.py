def fatorial(n):
    fat = 1
    for numero in range(2, n + 1):
        fat *= numero

    return fat


def main():
    numero = int(input('Informe um numero -> '))
    print(f'O fatorial de {numero} é {fatorial(numero)}')

main()