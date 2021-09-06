lista = []
while True:
    num = int(input("Digite um valor : "))
    if num >= 0:
        if num in lista == False:
            lista.append(num)
        else:
            print("Já tem esse numero na lista!")
    else:
        break
print(lista.sort())