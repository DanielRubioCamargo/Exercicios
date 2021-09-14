import Pacote.libfuncoes

def verificar_Arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"rt")
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_Arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"wt+")
        arq.close()
    except:
        print("Erro ao criar arquivo!")
    else:
        print("Arquivo {} criado com sucesso!".format(nomeArquivo))

def mostrar_Arquivo(nomeArquivo,msg = "Arquivo"):
    try:
        arq = open(nomeArquivo,"rt")
    except:
        print("Erro ao abrir o arquivo!")
    else:
        Pacote.libfuncoes.cabecalho(msg)
        print(arq.read())

