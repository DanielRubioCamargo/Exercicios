from Pack.libfuncoes import *

def criar_arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"wt")
        arq.close()
    except:
        print("\033[1;31mErro ao criar arquivo!\033[m")
    else:
        print("\033[1;32mArquivo {} criado com sucesso!\033[m".format(nomeArquivo))

def verificar_arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"rt")
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def registrar_novo_aluno(nomeArquivo,nomeAluno = "desconhecido",notaAluno = 0.0):
    try:
        arq = open(nomeArquivo,"at")
    except:
        print("\033[1;31mErro ao abrir o arquivo para edição!\033[m")
    else:
        try:
            arq.write("{};{}\n".format(nomeAluno,notaAluno))
        except:
            print("\033[1;31mErro ao registrar novo aluno!\033[m")
        else:
            print("\033[1;32m{} registrado(a) com sucesso!\033[m".format(nomeAluno))
        arq.close()

def mostrar_conteudo_arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"rt")
    except:
        print("\033[1;31mErro ao abrir o arquivo!\033[m")
    else:
        criar_cabecalho("Dados dos alunos")
        for linha in arq:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print("\033[1;34mNome : {} | Nota : {}\033[m".format(dado[0],dado[1]))
    arq.close()

def recarregar_dados_perdidos(nomeArquivo,lista):
    try:
        arq = open(nomeArquivo,"rt")
    except:
        print("\033[1;31mErro ao passar os valores do arquivo para a lista!\033[m")
    else:
        for linha in arq:
            dado = linha.split(";")
            lista.append(float(dado[1]))