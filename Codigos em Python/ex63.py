a = int(input("Numero : "))
b = int(input("Numero : "))
c = int(input("Numero : "))
tupla = (a,b,c)
cont9 = 0
for i in tupla:
    if i == 9:
        cont9 += 1
    if i%2==0:
        print("Numero {} é par!".format(i))
print("Obteve-se {} numeros 9!".format(cont9))
print(tupla.index(3))