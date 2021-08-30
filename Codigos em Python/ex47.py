numero = int(input("Insira um numero : "))
contPrimo = 0
for i in range(1,numero+1,1):
    if numero%i==0:
        contPrimo+=1
if contPrimo > 2:
    print("Não é primo!")
else:
    print("É primo!")