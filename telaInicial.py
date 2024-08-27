import telaGerente
import telaLer
import telaRemover
import telaAtualizar

while(True):
    print("MENU PRINCIPAL")
    print("1 - Cadastrar novo jogo")
    print("2 - Ver jogos cadastrados")
    print("3 - Deletar jogos")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        telaGerente.abrir()
    elif opcao == 2:
        telaLer.abrir()
    elif opcao == 3:
        telaRemover.abrir()
    elif opcao == 4:
        telaAtualizar.abrir()
    else:
        print("Opção inválida")

#1 - Cadastrar
#2 - Ler
#3 - Atualizar
#4 - Deletar