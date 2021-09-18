def convert_To_Negative(valor):
    if valor >= 0:
        return valor
    return abs(valor)

def concatenar_Nomes(nome,sobrenome):
    return nome + " " + sobrenome

def criar_Menu(lista):
    for i,c in enumerate(lista):
        print("{} -> {}".format(i+1,c))

opcoes = ["Somar","Subtrair","Multiplicar","Dividir","Sair do programa"]

escolha2 = ""

while escolha2 != "N":
    v1 = int(input("Valor 1 : "))
    v2 = int(input("Valor 2 : "))
    resultado = 0
    criar_Menu(opcoes)
    escolha = int(input("Opção : "))
    if escolha == 1:
        resultado = v1 + v2
    elif escolha == 2: 
        resultado = v1 - v2
    elif escolha == 3:
        resultado = v1 * v2
    elif escolha == 4:
        resultado = v1 / v2
    elif escolha == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")
    print("Resultado : {}".format(resultado))
    escolha2 = str(input("Deseja continuar? [S/N] : ")).upper().strip()