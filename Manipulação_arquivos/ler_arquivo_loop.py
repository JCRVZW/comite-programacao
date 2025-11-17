try:
    with open("meu_nome.txt", "r") as f:
       for linha in f:
           print(linha())
except FileNotFoundError:
    print("Arquivo não encontrado.")