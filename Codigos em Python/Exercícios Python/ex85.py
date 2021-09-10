resposta = ""
while resposta != "FIM":
    print("[1]len\n[2]print\n[3]input\n[4]strip")
    resposta2 = int(input("Qual você quer saber : "))
    if resposta2 == 1:
        help(len)
    elif resposta2 == 2:
        help(print)
    elif resposta2 == 3:
        help(input)
    elif resposta2 == 4:
        help(sorted)
    else:
        print("Inválido!")
    resposta = str(input("Digite FIM para finalizar ou outra coisa para continuar : ")).strip().upper()
