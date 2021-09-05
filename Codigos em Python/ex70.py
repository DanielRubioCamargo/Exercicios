#Primeiro e ultimo termos tem que ser parenteses!
expressao = str(input("Digite uma expressão entre parenteses : ")).strip()
while expressao[0] != "(" and expressao[len(expressao)-1] != ")":
    expressao = str(input("Incorreto! Digite a expressão entre parenteses : "))
print(expressao)