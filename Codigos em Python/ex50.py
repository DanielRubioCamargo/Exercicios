nome = ""
sexo = ""
idade = 0
mediaIdades = 0
acmIdades = 0
maiorIdade = 0
nomeHomemMaisVelho = ""
qtdMulheresMenores20 = 0
for i in range(0,4,1):
    nome = str(input("Qual é o seu nome : "))
    sexo = str(input("Qual é o seu sexo (M/F): "))
    idade = int(input("Qual é a sua idade : "))
    acmIdades += idade
    if sexo == "M" and idade > maiorIdade:
        nomeHomemMaisVelho = nome
    if sexo == "F" and idade < 20:
        qtdMulheresMenores20 += 1
mediaIdades = acmIdades/4
print("Media de idades : {}".format(mediaIdades))
print("Homem mais velho : {}".format(nomeHomemMaisVelho))
print("Quantidade de mulheres com idade inferior a 20 : {}".format(qtdMulheresMenores20))

