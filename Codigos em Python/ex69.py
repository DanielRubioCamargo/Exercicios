numeros = list()
cont = 0
while True:
    numeros.append(int(input("Insira um numero : ")))
    escolha = str(input("Quer continuar? : ")).upper().strip()
    cont += 1
    if escolha == "S":
        pass
    else:
        break
print(numeros)
if 5 in numeros:
    print("Ha o valor 5 na lista")
print("Foram digitados {} numeros!".format(cont))
numeros.sort(reverse = True)
print(numeros)