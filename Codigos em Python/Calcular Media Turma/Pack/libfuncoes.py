def criar_linha(tamanho = 40):
    print("-"*tamanho)

def criar_cabecalho(nome = "vazio",tamanho = 40):
    criar_linha(tamanho)
    print("\033[1;36m{}\033[m".format(nome.center(tamanho)))
    criar_linha(tamanho)

def criar_menu(listaOpcoes,nomeMenu = "Menu",tamanho = 40):
    criar_linha(tamanho)
    print("\033[1;36m{}\033[m".format(nomeMenu.center(tamanho)))
    criar_linha(tamanho)
    for i,c in enumerate(listaOpcoes):
        print("\033[1;35m{}\033[m --> {}".format(i+1,c))
    criar_linha(tamanho)

def calcular_media(listaNotas):
    acmNotas = 0.0
    qtdAlunos = len(listaNotas)
    for c in listaNotas:
        acmNotas += c
    try:
        mediaFinal = acmNotas/qtdAlunos
    except ZeroDivisionError:
        print("\033[1;31mNão se pode dividir algo por 0, provavelmente não há alunos registrados!\033[m")
    else:
        return mediaFinal

def leia_int(msg):
    try:
        valor = int(input(msg))
    except:
        print("\033[1;31mValor não é inteiro!\033[m")
    else:
        return valor