from funcoes import *

#Programa que lista nomes de pessoas e grava em um arquivo de texto (.txt)

def main():
    opcoes = ["Cadastrar nova pessoa","Exibir todas as pessoas","Deletar dados da lista","Sair do sistema"]
    arquivo = "teste.txt"
    if verificar_arquivo(arquivo) == False:
        criar_arquivo(arquivo)
    criar_cabecalho("\033[1;35mBem vindo!\033[m",60,True)
    while(True):
        criar_menu(opcoes,"Opções")
        try:
            opcao = int(input("Insira sua opção : "))
        except:
            print("\033[1;31mErro de digitação e/ou tipo de dado!\033[m")
        else:
            if opcao == 1:
                nomePessoa = str(input("Insira o nome da pessoa : "))
                adicionar_nova_pessoa(arquivo,nomePessoa)
            elif opcao == 2:
                exibir_pessoas(arquivo)
            elif opcao == 3:
                limpar_dados(arquivo)
            elif opcao == 4:
                print("\033[1;33mSaindo do sistema...\033[m")
                break
            else:
                print("\033[1;31mOpção inválida!\033[m")


if __name__ == "__main__":
    main()