from funcoes import *


def main():
    opcoes = ["Cadastrar nova pessoa","Exibir todas as pessoas","Deletar dados da lista","Sair do sistema"]
    arquivo = "teste.txt"
    if verificar_arquivo(arquivo) == False:
        criar_arquivo(arquivo)
    while(True):
        criar_menu(opcoes,"Opções")
        try:
            opcao = int(input("Insira sua opção : "))
        except:
            print("Erro de digitação e/ou tipo de dado!")
        else:
            if opcao == 1:
                nomePessoa = str(input("Insira o nome da pessoa : "))
                adicionar_nova_pessoa(arquivo,nomePessoa)
            elif opcao == 2:
                exibir_pessoas(arquivo)
            elif opcao == 3:
                limpar_dados(arquivo)
            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")


if __name__ == "__main__":
    main()