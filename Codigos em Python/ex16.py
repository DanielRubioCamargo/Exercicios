import random
aluno1 = int(input("Numero do primeiro aluno : "))
aluno2 = int(input("Numero do segundo aluno : "))
aluno3 = int(input("Numero do terceiro aluno : "))
aluno4 = int(input("Numero do quarto aluno : "))
alunoEscolhido = random.randint(aluno1,aluno4)
print("Aluno esolhido : {}".format(alunoEscolhido))