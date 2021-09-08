from random import randint
from time import sleep
jogos = list()
numeros  = list()
qtdJogos = int(input("Insira a quantidade de jogos para serem mostrados : "))
for i in range(0,qtdJogos,1):
    for j in range(0,6,1):
        numeros.append(randint(1,60))
    if(i != 0):
        for k in range(0,i,1):
            while(numeros == jogos[k]):
                for j in range(0,6,1):
                    numeros.append(randint(1,60))
    jogos.append(numeros[:])
    numeros.clear()
for i,c in enumerate(jogos):
    print("Jogada {} : {}".format(i+1,jogos[i]))
    sleep(1.5)