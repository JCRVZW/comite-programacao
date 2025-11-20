def boletim(nome, n1, n2, n3):
    media = (n1 + n2 + n3) / 3

        
    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"
   

    return {'nome': nome, 'media': media, 'situacao': status} 

aluno = boletim("Shevchenko", 7.0, 7.6, 7.86)
print(aluno)
with open ('boletim.txt', 'w') as arquivo:

    arquivo.write (f"Nome: {aluno['nome']}\n")
    arquivo.write (f"Média: {aluno['media']:.2f}\n")
    arquivo.write (f"Situação: {aluno['situacao']}\n")