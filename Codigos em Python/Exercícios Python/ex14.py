from math import pow,sqrt
catetoOposto = float(input("Digite o valor do cateto oposto : "))
catetoAdjacente = float(input("Digite o valor do cateto adjacente : "))
hipotenusa = sqrt((pow(catetoOposto,2) + pow(catetoAdjacente,2)))
print("A hipotenusa mede {:.2f}".format(hipotenusa))