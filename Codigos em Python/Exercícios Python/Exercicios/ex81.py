def maior(*valores):
    maior = 0
    for i,c in enumerate(valores):
        if i == 0:
            maior = c
        if c > maior:
            maior = c
    print("Maior valor encontrado : {}".format(maior))


maior(1,7,4,8,3,4,99,55,34,67,32,78)