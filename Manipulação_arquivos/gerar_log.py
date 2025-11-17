from datetime import datetime

def gerar_logs():
    with open("log.txt", "w") as arquivo:
        for i in range(3):
            agora = datetime.now()
            arquivo.write(f"Log {agora}: {i+1}\n")

def main():
    gerar_logs()
    
main()