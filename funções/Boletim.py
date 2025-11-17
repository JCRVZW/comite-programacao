def boletim(nome, n1, n2, n3):
    media = (n1 + n2 + n3) / 3

    status = ""
        
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
   

def main():
    nome_aluno = input("Informe o nome do aluno -> ")
    nota1 = float(input("Informe a primeira nota -> "))
    nota2 = float(input("Informe a segunda nota -> "))
    nota3 = float(input("Informe a terceira nota -> "))