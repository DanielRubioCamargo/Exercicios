precoInicial = float(input("Preço inicial : "))
formaPagamento1 = str(input("Forma de pagamento (A vista / Parcelado) : ")).strip()
formaPagamento2 = ""
vezes = 0
precoFinal = 0
desconto = 0
juros = 0
if formaPagamento1 == "A vista":
    formaPagamento2 = str(input("Qual a forma de pagamento real (Dinheiro/Cheque/Cartão)"))
    if formaPagamento2 == "Dinheiro" or formaPagamento2 == "Cheque":
        desconto = 10
    elif formaPagamento2 == "Cartão":
         desconto = 5
    else:
        print("Não foi aceito!")
elif formaPagamento1 == "Parcelado":
    vezes = int(input("Em quantas vezes no cartão ? : "))
    if vezes == 2:
        desconto = 0
        juros = 0
    elif vezes >= 3:
        juros = 20
    else:
        print("Quantidade rejeitada!")
else:
    print("Não existe essa forma de pagamento!")
precoFinal = precoInicial - (precoInicial*desconto/100) + (precoInicial*juros/100)
print("O preço final será : R${:.2f}".format(precoFinal))