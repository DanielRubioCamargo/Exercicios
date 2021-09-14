import Pacote.libfuncoes
import Pacote.libarquivo
from time import sleep

arq = "teste.txt"
opcoes = ["Ver pessoas cadastradas","Cadastrar nova pessoa","Sair do sistema"]
if Pacote.libarquivo.verificar_Arquivo(arq) == False:
    arquivo = Pacote.libarquivo.criar_Arquivo(arq)

while True:
    menu = Pacote.libfuncoes.menu(opcoes)
    escolha = Pacote.libfuncoes.leiaInt("Insira sua escolha : ")
    if escolha == 1:
        #Logica para mostrar pessoas cadastradas
        Pacote.libarquivo.mostrar_Arquivo(arq)
    elif escolha == 2:
        #Logica para cadastrar nova pessoa
        pass
    elif escolha == 3:
        print("\033[1;35mSaindo do sistema...\033[m")
        break
    else:
        print("\033[1;31mValor inválido! Tente novamente...\033[m")
    sleep(2)