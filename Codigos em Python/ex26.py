distancia = float(input("Qual a distancia da viagem em quilometros : "))
preco = 0.0
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45
print("Preço : R${:.2f}".format(preco))