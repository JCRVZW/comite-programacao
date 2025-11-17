from shutil import move


def copiar_arquivo():
    move ('teste.txt', 'docs/teste.txt')


def main():
    copiar_arquivo()

main()