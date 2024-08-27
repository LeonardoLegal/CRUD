import csv
from jogo import Jogo

def escreveArquivo(desenvolvedora, nome, preco, estoque, plataforma, publicadora):
    with open('jogos.csv', 'a', newline='', encoding='utf-8', errors='ignore') as csvfile:
        escreve = csv.writer(csvfile, delimiter=',')
        escreve.writerow([desenvolvedora, nome, preco, estoque, plataforma, publicadora])
        print("### JOGO ", nome, "adicionado com sucesso! ###")

contas = []
def abrir():
    print("### BEM VINDO A TELA DE CADASTRO DE JOGOS ###")
    print("\nNOVO USUÁRIO:")
    nome = input("Digite o título do jogo: \n")
    desenvolvedora = input("Digite a empresa desenvolvedora do jogo: \n")
    preco = float(input("Digite o valor do jogo: \n"))
    estoque = int(input("Digite o estoque disponível do jogo: \n"))
    plataforma = input("Digite as plataformas que suportam o jogo: \n")
    publicadora = input("Digite a publicadora do jogo: \n")
    novoJogo = Jogo(nome, desenvolvedora, preco, estoque, plataforma, publicadora)
    
    escreveArquivo(nome, desenvolvedora, preco, estoque, plataforma, publicadora)
    contas.append(novoJogo)