velocidade = float(input("Velocidade do veículo : "))
multa = 0.0
if velocidade > 80.0:
    multa = (velocidade-80)*7
    print("Multado! Valor da multa : R${:.2f}".format(multa))
else:
    print("Velocidade na faixa!")