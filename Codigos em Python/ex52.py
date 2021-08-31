from random import randint
numeroComputador = randint(1,5)
tentativas = 1
numeroEscolha = int(input("Escolha um numero de 1 a 5 : "))
while (numeroEscolha != numeroComputador):
    numeroEscolha = int(input("Numero errado! Tente novamente : "))
    tentativas += 1
print("Boa! Foram necessarias {} tentativas!".format(tentativas))