nome = str(input("Digite seu nome : ")).lower().strip()
vogal = 0
for i in range(0,len(nome),1):
    if (nome[i] == "a") or (nome[i] == "i") or (nome[i] == "e") or (nome[i] == "o") or (nome[i] == "u"):
        print(nome[i])
        vogal += 1
print("Foram achadas {} vogais!".format(vogal))