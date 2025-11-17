def listar_vogais(texto):
    vogais = 'aeiouAEIOU'
    resultado = []
    for char in texto:
        if char in vogais:
            resultado.append(char)
    return resultado
print(listar_vogais(input("Digite um texto: ")))
 