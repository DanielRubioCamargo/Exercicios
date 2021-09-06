sexo = str(input("Insira o sexo : ")).strip().upper()[0]
while(sexo not in "MF"):
    sexo = str(input("Valor inválido! Insira o sexo : "))
print("FIM DO PROGRAMA!")