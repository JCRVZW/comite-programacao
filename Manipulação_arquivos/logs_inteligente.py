def ler_logs(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        
     logs = arquivo.readlines()

     resultado = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}

     for linha in logs:
         if 'INFO' in linha:
             resultado['INFO'] += 1
         elif 'WARNING' in linha:
             resultado['WARNING'] += 1
         elif 'ERROR' in linha:
             resultado['ERROR'] += 1

    return resultado 

def gerar_relatorio(resultados):
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write("Relatório de Logs\n")
        for chave, valor in resultados.items():
            arquivo.write(f"existen {valor} ocorrencias do log {chave}\n")

    print("Relatorio de logs")
    for chave, valor in resultados.items():
        print(f"existen {valor} ocorrencias do log {chave}")

def main():
    nome_arquivo = 'log_desafio.txt'  
    resultados = ler_logs(nome_arquivo)
    gerar_relatorio(resultados)

main()