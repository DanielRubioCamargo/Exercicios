from random import randint
vitorias = 0
escolha = ""
numero = 0
numeroComputador = 0
soma = 0
while True:
    escolha = str(input("Qual a sua escolha ? (PAR/IMPAR) : ")).upper().strip()
    numero = int(input("Qual numero : "))
    numeroComputador = randint(1,10)
    soma = numero + numeroComputador
    if (escolha == "PAR" and soma%2==0) or (escolha == "IMPAR" and soma%2==1):
        vitorias += 1
    else:
        print("Perdeu! O valor deu {} porque eu escolhi o numero {}".format(soma,numeroComputador))
        break
print("Vitorias consecutivas : {}".format(vitorias))