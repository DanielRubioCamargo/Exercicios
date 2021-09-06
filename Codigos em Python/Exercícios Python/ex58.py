numero = 0
while True:
    numero = int(input("Insira um numero (Flag = Qualquer numero negativo) : "))
    if numero < 0:
        break
    else:
        for i in range(0,10,1):
            print("{}X{}={}".format(numero,i+1,(i+1)*numero))
    