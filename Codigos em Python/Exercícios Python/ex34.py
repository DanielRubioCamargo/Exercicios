idade = int(input("Insira sua idade : "))
if idade < 18:
    print("Ainda vai se alistar daqui {} anos!".format(18-idade))
elif idade == 18:
    print("Hora de se alistar!")
else:
    print("Já passou o tempo de alistamento!\nJa se passou {} anos!".format(idade-18))
