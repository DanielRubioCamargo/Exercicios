def criar_cabecalho(nome = "Cabeçalho",tamanhoLinha = 60):
    print("-"*tamanhoLinha)
    print(nome.center(tamanhoLinha))
    print("-"*tamanhoLinha)


def criar_menu(lista : list,nome = "Menu",tamanhoLinha = 60):
    print("-"*tamanhoLinha)
    print(nome.center(tamanhoLinha))
    print("-"*tamanhoLinha)
    for i,c in enumerate(lista):
        print("{} - {}".format(i+1,c))
    print("-"*tamanhoLinha)


def criar_arquivo(nomeArquivo : str):
    arq = open(nomeArquivo,"w")
    arq.close()


def adicionar_nova_pessoa(arquivo,nome : str):
    arq = open(arquivo,"a")
    arq.write("{}\n".format(nome))
    arq.close()


def exibir_pessoas(arquivo):
    criar_cabecalho("Pessoas inseridas")
    arq = open(arquivo,"r")
    for i,c in enumerate(arq):
        print("{} -> {}".format(i+1,c))
    arq.close()


def verificar_arquivo(arquivo) -> bool:
    try:
        arq = open(arquivo,"r")
        arq.close()
    except(FileNotFoundError):
        return False
    else:
        return True