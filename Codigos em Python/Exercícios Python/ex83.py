def voto(anoNascimento):
    if anoNascimento < 16:
        print("Negado!")
    elif anoNascimento >= 16 and anoNascimento < 18:
        print("Opicional!")
    else:
        print("Obrigatório!")


voto(17)