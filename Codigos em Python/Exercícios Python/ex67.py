numeros = list()
par = list()
impar = list()
for i in range(0,10,1):
    numeros.append(int(input("Digite um numero : ")))
    if numeros[i]%2==0:
        par.append(numeros[i])
    else:
        impar.append(numeros[i])
par.sort()
impar.sort()
print("Pares : {}\nImpares : {}".format(par,impar))