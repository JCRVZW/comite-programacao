import json


def salvar_dicionario(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo)

def main():
    dicionario_salvar = {
        'nome': 'Shevchenko',
        'idade': 15,
        'cidade': 'Sapucaia do Sul'
    }
    salvar_dicionario(dicionario_salvar, 'teste.json')

main()