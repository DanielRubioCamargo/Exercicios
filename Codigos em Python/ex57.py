numero = qtd = soma = 0
while True:
    numero = int(input("Digite um numero : "))
    if numero == 999:
        break
    else:
        qtd += 1
        soma += numero
print("Foram inseridos {} numeros! A soma deles é {}!".format(qtd,soma))