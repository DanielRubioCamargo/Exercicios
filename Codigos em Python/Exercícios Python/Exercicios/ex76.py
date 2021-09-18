from random import randint
from time import sleep
dadosJogadores = dict()
jogadas = list()
maior = 0
vencedor = ""
for i in range(0,4):
    nome = str(input("Nome : "))
    valor = randint(1,6)
    print("Jogando o dado...")
    sleep(1.5)
    print("Valor do dado : {}".format(valor))
    dadosJogadores = {"nome":nome,"valor":valor}
    jogadas.append(dadosJogadores.copy())
    dadosJogadores.clear()
for i,c in enumerate(jogadas):
    if(i == 0):
        maior = c["valor"]
        vencedor = c["nome"]
    if(c["valor"] > maior):
        maior = c["valor"]
        vencedor = c["nome"]
print("O vencedor é {} com uma jogada com o dado valendo {}".format(vencedor,maior))