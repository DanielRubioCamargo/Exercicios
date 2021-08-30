numero = int(input("Qual numero : "))
qtd = int(input("Até qual tabuada : "))
for i in range(1,qtd+1,1):
    print("{}X{}={}".format(i,numero,i*numero))