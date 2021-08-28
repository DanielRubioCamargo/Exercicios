salario = float(input("Digite o valor de seu salário : "))
aumento = 0.0
if salario > 1250.0:
    aumento = 10
else:
    aumento = 15
novoSalario = salario + (salario*(aumento/100))
print("Novo salário (com aumento de {} porcento) : R${:.2f}".format(aumento,novoSalario))