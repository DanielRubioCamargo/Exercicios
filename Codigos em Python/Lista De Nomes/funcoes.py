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
    try:
        arq = open(nomeArquivo,"w")
        arq.close()
    except:
        print("Erro ao criar arquivo!")
    else:
        print("Arquivo criado com sucesso!")


def adicionar_nova_pessoa(arquivo,nome : str):
    try:
        arq = open(arquivo,"a")
        arq.write("{}\n".format(nome))
        arq.close()
    except:
        print("Erro! Não foi possível adicionar o(a) {} na lista!".format(nome.title().strip()))
    else:
        print("{} adicionado(a) com sucesso!".format(nome.title().strip()))


def exibir_pessoas(arquivo):
    try:
        criar_cabecalho("Pessoas inseridas")
        arq = open(arquivo,"r")
        for i,c in enumerate(arq):
            print("{} -> {}".format(i+1,c.title().strip()))
        arq.close()
    except:
        print("Erro ao exibir lista de pessoas!")


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
        print("Erro ao deletar dados da lista!")
    else:
        print("Dados da lista deletados com sucesso!")
