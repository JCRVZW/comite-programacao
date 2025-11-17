try:
    with open("meu_nome.txt", "r") as f:
       print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado.")