def valor():
    return int(input('Informe um valor -> '))


def main():
    try:
        vl = valor()
    except ValueError:
        print('Valor invalido!', end='  ')
        print('Necessario um valor inteiro!')
    else:
        print(f'Valor informado: {vl}')

        
main()