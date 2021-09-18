nomeArquivo = "arquivo.txt"
numeroPessoas = int(input("Quantidade de pessoas : "))
arquivo = open(nomeArquivo,"w")
for i in range(1,numeroPessoas+1,1):
    nome = str(input("Insira seu nome : "))
    arquivo.write("{} --> {}\n".format(i,nome))
arquivo = open(nomeArquivo,"rt")
for i in arquivo:
    i = i.replace("\n","")
    print(i)
arquivo.close()    