from time import sleep
inicio = int(input("Qual é o valor inicial da contagem? : "))
fim = int(input("Qual é o valor final da contagem? : "))
passo = int(input("Qual é o passo da contagem? : "))
for i in range(inicio,fim,passo):
    print(i)
    sleep(1.5)
print("BOOOM!")