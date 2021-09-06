soma = 0
for i in range(0,6,1):
    numero = int(input("Insira um numero : "))
    if numero%2==0:
        soma+=numero
print("Soma = {}".format(soma))