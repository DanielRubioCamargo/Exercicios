from time import sleep
def contador(inicio,fim,passo):
    for i in range(inicio,fim,passo):
        print(i)
        sleep(1.5)

contador(0,11,1)
contador(10,-1,-2)
inicio = int(input("Qual o valor do inicio : "))
fim = int(input("Qual o valor final : "))
passo = int(input("Qual o valor do passo : "))
contador(inicio,fim,passo)