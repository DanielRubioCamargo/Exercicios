aluno = list()
notas = list()
classe = list()
resposta = ""
nome = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0
cont = 0
while resposta != "N":
    nome = str(input("Qual o seu nome : ")).strip()
    nota1 = float(input("Nota 1 : "))
    nota2 = float(input("Nota 2 : "))
    notas.append(nota1)
    notas.append(nota2)
    media = (nota1+nota2)/2
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    classe.append(aluno[:])
    aluno.clear()
    notas.clear()
    cont += 1
    resposta = str(input("Quer continuar[S/N] : ")).upper().strip()
print("------------------------------------")
print("Numero   |   Nome   |   Media  ")
for i,c in enumerate(classe):
    print("{}          {}          {}".format(i+1,c[0],c[2]))
valor = 0
numero = 0
while valor != 999:
    numero = int(input("Gostaria de ver as notas de algum aluno? [S/N] : (999 para cancelar)"))
    if valor != 999:
        print("Notas do/da {} : {}".format(classe[numero-1][0],classe[numero-1][1]))