def numero_primo(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    teste = 13
    if numero_primo(teste):
        print(f"{teste} é um número primo.")
    else:
        print(f"{teste} não é um número primo.")
main()