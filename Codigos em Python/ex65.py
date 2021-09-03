lista = list()
maior = 0
menor = 0
for i in range(0,5):
    lista.append(int(input("Digite um valor : ")))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
print(lista)
print("Maior = {}\nMenor = {}".format(maior,menor))