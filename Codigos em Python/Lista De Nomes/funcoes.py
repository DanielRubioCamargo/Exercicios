def criar_cabecalho(nome = "Cabeçalho",tamanhoLinha = 60,eEspecial = False):
    if eEspecial == False:
        print("-"*tamanhoLinha)
        print(nome.center(tamanhoLinha))
        print("-"*tamanhoLinha)
    else:
        print("-=-"*20)
        print(nome.center(tamanhoLinha))
        print("-=-"*20)


def criar_menu(lista : list,nome = "Menu",tamanhoLinha = 60):
    print("-"*tamanhoLinha)
    print("\033[1;34m{}\033[m".format(nome.center(tamanhoLinha)))
    print("-"*tamanhoLinha)
    for i,c in enumerate(lista):
        print("\033[1;33m{}\033[m - {}".format(i+1,c))
    print("-"*tamanhoLinha)


def criar_arquivo(nomeArquivo : str):
    try:
        arq = open(nomeArquivo,"w")
        arq.close()
    except:
        print("\033[1;31mErro ao criar arquivo!\033[m")
    else:
        print("\033[1;32mArquivo criado com sucesso!\033[m")


def adicionar_nova_pessoa(arquivo,nome : str):
    try:
        arq = open(arquivo,"a")
        arq.write("{}\n".format(nome))
        arq.close()
    except:
        print("\033[1;31mErro! Não foi possível adicionar o(a) {} na lista!\033[m".format(nome.title().strip()))
    else:
        print("\033[1;32m{} adicionado(a) com sucesso!\033[m".format(nome.title().strip()))


def exibir_pessoas(arquivo):
    try:
        criar_cabecalho("Pessoas inseridas")
        arq = open(arquivo,"r")
        for i,c in enumerate(arq):
            print("{} -> {}".format(i+1,c.title().strip()))
        arq.close()
    except:
        print("\033[1;31mErro ao exibir lista de pessoas!\033[m")


def verificar_arquivo(arquivo) -> bool:
    try:
        arq = open(arquivo,"r")
        arq.close()
    except(FileNotFoundError):
        return False
    else:
        return True


def limpar_dados(arquivo : str):
    try:
        arq = open(arquivo,"w")
        arq.close()
    except:
        print("\033[1;31mErro ao deletar dados da lista!\033[m")
    else:
        print("\033[1;32mDados da lista deletados com sucesso!\033[m")
