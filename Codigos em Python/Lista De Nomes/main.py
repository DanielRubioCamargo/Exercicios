from funcoes import *


def main():
    opcoes = ["Cadastrar nova pessoa","Exibir todas as pessoas","Sair do sistema"]
    arquivo = "teste.txt"
    if verificar_arquivo(arquivo) == False:
        criar_arquivo(arquivo)
    while(True):
        criar_menu(opcoes,"Opções")
        opcao = int(input("Insira sua opção : "))
        if opcao == 1:
            nomePessoa = str(input("Insira o nome da pessoa : "))
            adicionar_nova_pessoa(arquivo,nomePessoa)
        elif opcao == 2:
            exibir_pessoas(arquivo)
        elif opcao == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()