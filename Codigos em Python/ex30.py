lado1 = float(input("Medida do lado 1 : "))
lado2 = float(input("Medida do lado 2 : "))
lado3 = float(input("Medida do lado 3 : "))
if lado1 < lado2+lado3:
    if lado2 < lado1+lado3:
        if lado3 < lado1+lado2:
            print("É possível fazer um triangulo!")
        else:
            print("Não")
    else:
        print("Não")
else:
    print("Não")