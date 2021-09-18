from random import randint

numeros = list()

def somaPar(lst):
    soma = 0
    for i in lst:
        if i%2==0:
            soma+=i
    print("Soma dos valores pares : {}".format(soma))

def sorteio(n,lst):
    for i in range(0,n,1):
        valor = 0
        valor = randint(1,10)
        lst.append(valor)
        print(valor)
num = 5
sorteio(num,numeros)
somaPar(numeros)