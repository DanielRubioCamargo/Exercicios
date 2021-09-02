from random import randint
v1 = randint(1,20)
v2 = randint(1,20)
v3 = randint(1,20)
v4 = randint(1,20)
v5 = randint(1,20)
tupla = (v1,v2,v3,v4,v5)
novaTupla = sorted(tupla)
print(novaTupla)
menor = novaTupla[0]
maior = novaTupla[len(novaTupla)-1]
print("Maior valor da tupla : {}\nMenor valor da tupla : {}".format(maior,menor))