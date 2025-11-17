import os 

def add_arquivo(arquivo):
        os.mkdir(arquivo)
        print("criado com sucesso")
   

def main():
    nome_arquivo = input('Qual pasta deseja criar? ')
    add_arquivo(nome_arquivo)
main()