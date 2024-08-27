def abrir():
    import csv
    from jogo import Jogo
    jogos = []

    def ler_arquivo():
        with open('jogos.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
            linha = csv.reader(csvLeitura, delimiter=',')
            for coluna in linha:
                # ARMAZENAR OS PRODUTOS NUMA LISTA
                novoJogo = Jogo(coluna[0], coluna[1], coluna[2], coluna[3], coluna[4], coluna[5])
                jogos.append(novoJogo)




    def altera_dados():
        indice = int(input("Digite o índice do jogo a ser alterado:"))
        print("Digite apenas o atributo que você deseja alterar. Caso queira manter o valor antigo, apenas aperte ENTER")
        nome = input("Nome: ")
        desenvolvedora = input("Desenvolvedora: ")
        preco = input("Preço: ")
        plataformas = input("Plataformas: ")
        estoque = input("Estoque: ")
        publicadora = input("Publicadora: ")
        if nome != "":
            jogos[indice].nome = nome
        if desenvolvedora != "":
            jogos[indice].desenvolvedora = desenvolvedora
        if plataformas != "":
            jogos[indice].plataformas = plataformas
        if estoque != "":
            jogos[indice].estoque = estoque
        if publicadora != "":
            jogos[indice].publicadora = publicadora
        if preco != "":
            jogos[indice].preco = preco

    def escreve_arquivo():
        with open('jogos.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
            escrever = csv.writer(csvEscrita)
            for c in jogos:
                escrever.writerow([c.nome, c.desenvolvedora, c.plataformas, c.estoque, c.publicadora, c.preco])
            print(f"Arquivo atualizado! Jogos atualizados com sucesso!")


    ler_arquivo()
    altera_dados()
    escreve_arquivo()