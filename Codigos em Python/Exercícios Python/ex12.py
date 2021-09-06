preco = float(input("Insira o preço do produto : "))
novoPreco = preco - (preco*(5/100))
print("O novo preço com 5 porcento de desconto é : R${:.2f}".format(novoPreco))