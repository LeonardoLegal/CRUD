import csv
linhas = []
def abrir():
    indice = int(input("Digite o número do jogo a ser excluído: "))

    with open('jogos.csv', 'r', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
        leitor = csv.reader(csvLeitura, delimiter=',')
        for linha in leitor:
            linhas.append(linha)
    print(linhas)
    linhas.pop(indice - 1)
    print(linhas)

    with open('jogos.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
        escrever = csv.writer(csvEscrita)
        escrever.writerows(linhas)
        print(f"Arquivo atualizado! Jogo {indice} excluído com sucesso!")