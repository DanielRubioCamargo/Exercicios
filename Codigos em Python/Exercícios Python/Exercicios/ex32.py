valorDaCasa = float(input("Qual o valor da casa ? : "))
salario = float(input("Qual o seu salário ? : "))
tempo = int(input("Quantos anos para pagar ? : "))
mensalidade = valorDaCasa/tempo*12
if mensalidade > (salario*30/100):
    print("Empréstimo negado!")
else:
    print("Sucesso!")
