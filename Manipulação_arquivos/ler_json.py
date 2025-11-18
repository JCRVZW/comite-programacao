import json

def ler_arquivo_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
        for chave, valor in dados.items():
            print(f"{chave} | {valor}")

def main():
    nome_arquivo = 'teste.json'  
    ler_arquivo_json(nome_arquivo)

main()