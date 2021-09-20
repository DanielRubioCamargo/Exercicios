from Pack.libfuncoes import *
from Pack.libarquivo import *
from time import sleep

notas = list()
opcoes = ["Verificar alunos registrados","Registrar novo aluno","Calcular media da turma","Sair do sistema"]

arquivo = "notas.txt"

if verificar_arquivo(arquivo) == False:
    criar_arquivo(arquivo)

recarregar_dados_perdidos(arquivo,notas)

while True:
    menu = criar_menu(opcoes,"Opções")
    escolhaOpcao = leia_int("Insira uma das opções acima : ")
    if escolhaOpcao == 1:
        mostrar_conteudo_arquivo(arquivo)
    elif escolhaOpcao == 2:
        try:
            nome = str(input("Insira seu nome : "))
            nota = float(input("Insira sua nota : "))
        except:
            print("\033[1;31mErro ao receber os dados do aluno!\033[m")
        else:
            registrar_novo_aluno(arquivo,nome,nota)
            notas.append(nota)
    elif escolhaOpcao == 3:
        media = calcular_media(notas)
        try:
            print("\n\033[1;33mMedia geral da classe : {:.2f}\033[m\n".format(media))
        except:
            print("\033[1;31mErro ao calcular media!\033[m")
    elif escolhaOpcao == 4:
        print("\033[1;32mSaindo do sistema...\033[m")
        break
    else:
        print("\033[1;31mOpção inválida!\033[m")
    sleep(0.75)