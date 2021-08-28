from random import randint
numeroUsuario = int(input("Digite um numero de 1 até 5 : "))
numeroComputador = randint(1,5)
if numeroUsuario == numeroComputador:
    print("Parabens você acertou o numero!!!")
else:
    print("Errou kkkk eu escolhi o numero {}".format(numeroComputador))