def aumento(valor, porcentagem):
    novo_valor = valor + (valor * porcentagem / 100)
    return novo_valor

def main():
    valor = float(input("Digite o valor -> "))
    porcentagem = float(input("Digite a % -> "))

    novo_valor = aumento(valor, porcentagem)

    print(f"O novo valor é:", (novo_valor))
 

main()