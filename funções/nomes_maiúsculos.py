def upper(nomes):
   temp = []
   for nome in nomes:
     temp.append(nome.upper())
   return temp

def main():
    nomes = ['Shevchenko','Pedro','Ana','maria','paulo']
    nomes_maiusculos = []

    nomes_maiusculos = upper(nomes)
    for nome in nomes_maiusculos:
        print(nome)

main()