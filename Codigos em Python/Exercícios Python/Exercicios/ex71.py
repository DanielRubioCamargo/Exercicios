pessoas = list()
dados = list()
resposta = ""
qtdPessoas = 0
maisPesado = maisLeve = 0.0
pP = pL = ""
while resposta != "N":
    dados.append(str(input("Insira seu nome : ")))
    dados.append(float(input("Insira seu peso : ")))
    pessoas.append(dados[:])
    dados.clear()
    qtdPessoas += 1
    resposta = str(input("Quer continuar [S/N]? : ")).upper().strip()
print("Foram cadastradas {} pessoas!".format(qtdPessoas))
for i,c in enumerate(pessoas):
    print(c)
    if(i == 0):
        maisPesado = c[1]
        maisLeve = c[1]
        pP = c[0]
        pL = c[0]
    if(c[1] > maisPesado):
        maisPesado = c[1]
        pP = c[0]
    if(c[1] < maisLeve):
        maisLeve = c[1]
        pL = c[0]
print("A pessoa mais pesada é o/a {}".format(pP))
print("A pessoa mais leve é o/a {}".format(pL))