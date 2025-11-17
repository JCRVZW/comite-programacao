import os 
def del_arquivo(arquivo):
    try:
        
            os.remove(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def main():
    nome_arquivo = input('Qual arquivo deseja deletar? ')
    del_arquivo(nome_arquivo)
main()