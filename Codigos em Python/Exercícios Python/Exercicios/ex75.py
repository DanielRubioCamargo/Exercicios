aluno = dict()
classe = list()
resposta = ""
while resposta != "N":
    nome = str(input("Insira seu nome : "))
    media = float(input("Insira sua media : "))
    situacao = ""
    if(media < 6.0):
        situacao = "Ruim"
    else:
        situacao = "Boa"
    aluno = {"nome": nome,"media": media,"situacao": situacao}
    classe.append(aluno.copy())
    aluno.clear()
    resposta = str(input("Quer continuar ? [S/N] : ")).upper().strip()
resposta2 = str(input("Quer saber a situação de qual aluno? : "))
for i,c in enumerate(classe):
    if(resposta2 == c["nome"]):
        print("Situação de {} : {}".format(c["nome"],c["situacao"]))