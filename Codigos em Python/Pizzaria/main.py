#----------------------------------------------- TO DO ------------------------------------------------------
# Ideia principal : Crição de um programa capaz de gerenciar pedidos em uma pizzaria!
# O que fazer : 
# - Criar um menu (interface) para realização dos pedidos.
# - Confirmação do pedido caso o pagamento seja sucedido, caso não, cancelar o pedido.
# - Gerenciamento de produtos no estoque.
# - Gerção de código de pedido.
# - Medição de quantidade de pedidos de cada sabor, bebidas, etc.. para análise estatística.
# - Opção de feedback e avaliação do cliente (opcional para o usuário).
# - Opção de doação para a pizzaria.
# - Colorir terminal.
# - Correção de bugs.
#------------------------------------------------------------------------------------------------------------
# * 'KEYS' : PIZZA, SALGADA, DOCE, BEBIDA, REFRIGERANTE, CERVEJA, NOME, PEDIDO, CODIGO.
#------------------------------------------------------------------------------------------------------------

from funcoes import *

def main():

    optionList = ["Realizar um pedido","Verificar pedido","Fazer uma doação","Sair do sistema"]

    menuDictionary = {"PIZZA" : {"SALGADA" : ["FRANGO COM CATUPIRY","ATUM","PORTUGUESA","CALABRESA","QUEIJO"],"DOCE" : ["NUTELLA","DOCE DE LEITE","MORANGO COM CHOCOLATE"]}, "BEBIDA" : {"REFRIGERANTE" : ["GUARANÁ","COCA-COLA","PEPSI","FANTA LARANJA","FANTA UVA"],"CERVEJA": ["BRAHMA","SKOL","ITAIPAVA","AMSTEL"]}}

    ordersDictionary = {"NOME" : [],"PEDIDO" : [],"CODIGO" : []}

    bankAmount = 0.0
    orders = 0

    create_head("Bem vindo(a) a Pizzaria da Alegria!")

    while True:
        price = 0.0
        create_menu(optionList,"Opções")
        option = int(input("Insira sua opção : "))
        if option == 1:
            mKey = str(input("Insira 'Pizza' caso deseje pedir uma pizza ou 'Bebida' caso queira alguma bebida : ")).upper().strip()
            if mKey == "PIZZA":
                sKey = str(input("Insira 'Salgada' caso deseje pedir uma pizza salgada ou 'Doce' caso queira uma pizza doce : ")).upper().strip()
                if sKey == "SALGADA":
                    price = 60.5
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    choiceP1 = int(input("Insira sua opção em número : "))
                    if choiceP1 >= 0 and choiceP1 < len(menuDictionary[mKey][sKey]):
                        chosenProductP1 = choose_product(menuDictionary[mKey][sKey],choiceP1)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeP1 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeP1))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductP1)
                            ordersDictionary["CODIGO"].append(rCodeP1)
                            bankAmount += price
                            orders += 1
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                elif sKey == "DOCE":
                    price = 45.5
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    choiceP2 = int(input("Insira sua opção em número : "))
                    if choiceP2 >= 0 and choiceP2 < len(menuDictionary[mKey][sKey]):
                        chosenProductP2 = choose_product(menuDictionary[mKey][sKey],choiceP2)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeP2 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeP2))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductP2)
                            ordersDictionary["CODIGO"].append(rCodeP2)
                            bankAmount += price
                            orders += 1
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                else:
                    print("Não foi possível acessar o cardápio, entrada inválida!")
            elif mKey == "BEBIDA":
                sKey = str(input("Insira 'Refrigerante' caso deseje pedir um refrigerante ou 'Cerveja' caso queira uma cerveja : ")).upper().strip()
                if sKey == "REFRIGERANTE":
                    price = 12.5
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    choiceB1 = int(input("Insira sua opção em número : "))
                    if choiceB1 >= 0 and choiceB1 < len(menuDictionary[mKey][sKey]):
                        chosenProductB1 = choose_product(menuDictionary[mKey][sKey],choiceB1)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeB1 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeB1))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductB1)
                            ordersDictionary["CODIGO"].append(rCodeB1)
                            bankAmount += price
                            orders += 1
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                elif sKey == "CERVEJA":
                    price = 15.25
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    choiceB2 = int(input("Insira sua opção em número : "))
                    if choiceB2 >= 0 and choiceB2 < len(menuDictionary[mKey][sKey]):
                        chosenProductB2 = choose_product(menuDictionary[mKey][sKey],choiceB2)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeB2 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeB2))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductB2)
                            ordersDictionary["CODIGO"].append(rCodeB2)
                            bankAmount += price
                            orders += 1
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                else:
                    print("Não foi possível acessar o cardápio, entrada inválida!")
                    continue
            else:
                print("Não foi possível acessar o cardápio, entrada inválida!")
                continue
        elif option == 2:
            pass
        elif option == 3:
            amountToDonate = float(input("Insira a quantidade para doar : "))
            if amountToDonate > 0:
                bankAmount += amountToDonate
                print("Muito obrigado por doar R${} para a pizzaria!".format(amountToDonate))
            else:
                print("Para de brincadeira ae!")
        elif option == 4:
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()