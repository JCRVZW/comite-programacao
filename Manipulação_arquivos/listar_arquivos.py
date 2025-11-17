import os

def listar_arquivos():
    arquivos = os.listdir('.')
    for arquivo in arquivos:
        print(arquivo)

def main():
    listar_arquivos()

    
main()