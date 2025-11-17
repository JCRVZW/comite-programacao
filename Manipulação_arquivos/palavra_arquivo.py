def encontrar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo) as arquivo:
            texto = arquivo.readlines()
            cont = 0
            for linha in texto:
                if palavra.lower() in linha.lower():
                    cont += 1
                    print(f'palavra {palavra.lower()} encontrada na linha: {cont}')
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def main():
    nome_arquivo = 'texto.txt'
    palavra = input('Digite a palavra que deseja encontrar: ')
    encontrar_palavra(nome_arquivo, palavra)
                          
main()
              