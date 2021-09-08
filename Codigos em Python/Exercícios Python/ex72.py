numeros = list()
pares = list()
impares = list()
valor = 0
for i in range(0,7,1):  
    valor = int(input("Insira um valor : "))
    if(valor%2==0):
        pares.append(valor)
    else:
        impares.append(valor)
numeros.append(pares)
numeros.append(impares)
print("Valores como digitados : {}".format(numeros))
pares.sort()
impares.sort()
print("Valores em ordem crescente : {}".format(numeros))