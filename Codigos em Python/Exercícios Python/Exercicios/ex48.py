maiores = 0
menores = 0
for i in range(0,7,1):
    ano = int(input("Insira o ano de seu nascimento : "))
    if 2021-ano >= 18:
        maiores+=1
    else:
        menores+=1
print("Maioridade : {}\nMenores : {}".format(maiores,menores))