def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "impossível realizar uma divisão por 0"
    else:
        return "Operação inválida! "
def main():
    while True:
        n1 = float(input("informe o primeiro valor -> "))
        n2 = float(input("informe o segundo valor -> "))
        op = input("Qual a operação? | + | - | * | / | -> ")

        resultado = calcular(n1, n2, op)
        print(f'Resultado: {resultado}')
        continuar = input("Deseja realizar outra operação? (s/n) -> ")
        if continuar != 's':
            break
       
main()
