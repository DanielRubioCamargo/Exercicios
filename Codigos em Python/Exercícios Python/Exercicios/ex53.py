n1 = int(input("Digite um numero : "))
n2 = int(input("Digite outro numero : "))
print("::Menu::\n[1] - SOMAR\n[2] - MULTIPLICAR\n[3] - MAIOR\n[4] - SAIR DO PROGRAMA")
digito = 0
while(digito != 4):
    digito = int(input("Escolha um item do menu! : "))
    resultado = 0
    if(digito == 1):
        resultado = n1+n2
    elif(digito == 2):
        resultado = n1*n2
    elif(digito == 3):
        resultado = max(n1,n2)
    elif(digito == 4):
        pass
    else:
        print("Inválido!")
    print("Resultado : {}".format(resultado))