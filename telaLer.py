import csv
def abrir():
    with open('jogos.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor:
            print(f"## Jogo: {linha[0]} desenvolvido por {linha[1]}, Preço: R$ {linha[2]}. Estoque de {linha[3]}, suportado por ${linha[4]}, publicado por {linha[5]}.")