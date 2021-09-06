numero = int(input("Digite um numero : "))
fatorial = 1
contador = 0
while contador < numero:
    fatorial = fatorial * (numero - contador)
    contador += 1
print("Fatorial de {} é {}".format(numero,fatorial))