def calcular_ano_nascimento(idade, ano_atual):
    print(f'Você nasceu em {ano_atual - idade}.')

def main():
    idade = int(input("Digite sua idade: "))
    ano_atual = int(input("Digite o ano atual: "))
    calcular_ano_nascimento(idade, ano_atual)

main()
    