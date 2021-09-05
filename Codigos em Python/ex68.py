numeros = list()
for i in range(0,10):
    num = 0
    num = int(input("Insira um numero : "))
    if not(num in numeros):
        numeros.append(num)
numeros.sort()
print(numeros)