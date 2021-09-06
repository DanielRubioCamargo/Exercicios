from random import randint
escolha = str(input("Pedra, papel ou tesoura? : "))
escolhaNumericaComputador = randint(1,3)
escolhaReal = ""
if escolhaNumericaComputador == 1:
    escolhaReal = "Pedra"
elif escolhaNumericaComputador == 2:
    escolhaReal = "Papel"
else:
    escolhaReal = "Tesoura"
print("Computador escolheu : {}".format(escolhaReal))
if (escolha == "Pedra" and escolhaReal == "Tesoura") or (escolha == "Tesoura" and escolhaReal == "Papel") or (escolha == "Papel" and escolhaReal == "Pedra"):
    print("\033[0;32mUsuário Venceu!!!\033[m")
elif (escolhaReal == "Pedra" and escolha == "Tesoura") or (escolhaReal == "Tesoura" and escolha == "Papel") or (escolhaReal == "Papel" and escolha == "Pedra"):
    print("\033[0;31mComputador Dominou!!!\033[m")
else:
    print("\033[0;35mEmpate!\033[m")
print("FIM DO JOGO!")