import Pacote.libmetodos
from time import sleep

opcoes = ["Ver pessoas cadastradas","Cadastrar nova pessoa","Sair do sistema"]

while True:
    menu = Pacote.libmetodos.menu(opcoes)
    escolha = Pacote.libmetodos.leiaInt("Insira sua escolha : ")
    if escolha == 1:
        #Logica para mostrar pessoas cadastradas
        pass
    elif escolha == 2:
        #Logica para cadastrar nova pessoa
        pass
    elif escolha == 3:
        print("\033[1;35mSaindo do sistema...\033[m")
        break
    else:
        print("\033[1;31mValor inválido! Tente novamente...\033[m")
    sleep(2)