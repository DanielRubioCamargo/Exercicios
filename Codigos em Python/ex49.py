maior = 0.0
for i in range(0,5,1):
    peso = float(input("Peso : "))
    if peso > maior:
        maior = peso
print("O maior peso encontrado foi {}Kg".format(maior))