def exibir_nome_idade(nome, idade):
    return (f" Olá! {nome}, parabéns pelos seus {idade} anos!")

def main():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    boas_vindas = exibir_nome_idade(nome, idade)

    print(boas_vindas)

main()