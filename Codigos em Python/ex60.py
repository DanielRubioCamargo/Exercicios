nome = ""
valor = 0.0
maisBarato = ""
totalGasto = 0.0
qtdProdutosMaiores1000 = 0
cont = 0
resp = ""
while True:
    cont += 1 
    nome = str(input("Nome do produto : "))
    valor = float(input("Valor do produto : "))
    if cont == 1:
        maisBarato = nome
    totalGasto += valor
    if valor >= 1000:
        qtdProdutosMaiores1000 += 1
    resp = str(input("Quer continuar [S/N] : ")).upper().strip()
    if resp == "S":
        pass
    elif resp == "N":
        break
print("Total gasto : R${}\nProduto mais barato : {}\nQuantidade de produtos com mais de R$1000,0 de preço : {}".format(totalGasto,maisBarato,qtdProdutosMaiores1000))