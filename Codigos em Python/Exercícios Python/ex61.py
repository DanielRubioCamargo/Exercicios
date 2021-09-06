numerosPorExtenso = ("Zero","Um","Dois","Tres","Quatro","Cinco")
while True:
    numero = int(input("Digite um numero de 0 a 5 : "))
    if numero >= 0 and numero <= 5:
        break
    else:
        print("Incorreto!")
for i in range(0,len(numerosPorExtenso)):
    if numero == i:
        print(numerosPorExtenso[i])
