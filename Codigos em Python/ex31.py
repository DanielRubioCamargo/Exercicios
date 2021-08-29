#Extra
nome = str(input("Digite seu nome : "))
cor = str(input("Qual cor para colocar no seu nome [Vermelho,Verde,Amarelo,Roxo] : "))
codigoCor = ""
if cor == "Vermelho":
    codigoCor = "\033[0;31m"
else:
    if cor == "Verde":
        codigoCor = "\033[0;32m"
    else:
        if cor == "Amarelo":
            codigoCor = "\033[0;33m"
        else:
            if cor == "Roxo":
                codigoCor = "\033[0;35m"
            else:
                print("Não há essa cor!!!")
print("Nome : {}{}{}".format(codigoCor,nome,"\033[m"))