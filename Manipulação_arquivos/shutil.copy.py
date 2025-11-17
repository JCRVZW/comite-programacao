from shutil import copy


def copiar_arquivo():
    copy('texto.txt', 'texto_copiado.txt')


def main():
    copiar_arquivo()

main()