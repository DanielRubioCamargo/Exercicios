def opcoes_lista(lista:list):
    listaOpcoes = ["Ordem crescente","Ordem decrescente","Impares","Pares","Maiores que um número"]
    for i,c in enumerate(listaOpcoes):
        print("{} -> {}".format(i+1,c))
    op = int(input("Qual a sua opção? : "))
    if op == 1:
        print(sorted(lista))
    elif op == 2:
        print(sorted(lista,reverse=True))
    elif op == 3:
        for c in lista:
            if c%2==1:
                print(c)
    elif op == 4:
        for c in lista:
            if c%2==0:
                print(c)
    elif op == 5:
        valor = int(input("Qual será o valor : "))
        for c in lista:
            if c > valor:
                print(c)
    else: 
        print("Opção inválida")


def main():
    lista = [1, 1, 2, 3, 5, 8, 13, 21]
    opcoes_lista(lista)

if __name__ == "__main__":
    main()