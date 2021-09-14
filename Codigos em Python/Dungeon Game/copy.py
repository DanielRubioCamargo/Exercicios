from random import randint
numeroSala = 1
escolhaCaminho = 0
cont = 0
print("\nOlá aventureiro! :D\n")
print("--------------------------\nSala atual (inicial) : {}\n--------------------------".format(numeroSala))
while numeroSala != 9 and cont < 7:
    escolhaCaminho = int(input("Qual caminho você seguirá (se escolher algum diferente de 1 ou 2 será adicionado 1)?\n[1] Vermelho\n[2] Preto\nEscolha : "))
    if(numeroSala == 8 and escolhaCaminho == 2):
        print("\n* Você caiu na dungeon dos controladores do espaço-tempo! Teleportando para uma sala aleatória ... *\n")
        numeroSala = randint(1,5)
    elif(numeroSala == 6 or escolhaCaminho == 2):
        numeroSala += 2
    else:
        numeroSala += 1
    print("----------------------\nSua sala atual é : {}\n----------------------\n".format(numeroSala))
    cont = cont + 1
if(numeroSala == 9):
    print("Você venceu! Parabens por chegar na sala 9 !!!\n")
elif(cont >= 7):
    print("Você perdeu por excesso de jogadas!\n")
print("Total de jogadas : {}\n".format(cont))