from Pacote import funçoes,funçoes2

valor = float(input("Insira algum valor : "))
aumento = int(input("Insira o aumento : "))
diminuicao = int(input("Insira a diminuição : "))

print("Dobro : {}\nMetade : {}\nValor aumentado em {}% : {}\nValor diminuido em {}% : {}".format(funçoes2.dobro(valor),funçoes2.metade(valor),aumento,funçoes.aumentar(valor,aumento),diminuicao,funçoes.diminuir(valor,diminuicao)))