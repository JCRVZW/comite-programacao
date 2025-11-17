def inverter_string(s):
    return s[::-1]

def main():
    texto = "Arroz com feijão é bom"
    texto_invertido = inverter_string(texto)
    print(f"Texto original: {texto}")
    print(f"Texto invertido: {texto_invertido}")

main()