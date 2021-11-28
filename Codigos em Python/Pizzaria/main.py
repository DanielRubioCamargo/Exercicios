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
# * 'KEYS' : PIZZA, SALGADA, DOCE, BEBIDA, REFRIGERANTE, CERVEJA, NOME, PEDIDO, CODIGO, Products, Amount.
#------------------------------------------------------------------------------------------------------------

from matplotlib.pyplot import draw
from funcoes import *
import pandas as pd
from IPython.display import display

def main():

    optionList = ["Realizar um pedido","Verificar pedido","Fazer uma doação","Sair do sistema"]

    menuDictionary = {"PIZZA" : {"SALGADA" : ["FRANGO COM CATUPIRY","ATUM","PORTUGUESA","CALABRESA","QUEIJO"],"DOCE" : ["NUTELLA","DOCE DE LEITE","MORANGO COM CHOCOLATE", "BANANA COM CHOCOLATE"]}, "BEBIDA" : {"REFRIGERANTE" : ["GUARANÁ","COCA-COLA","PEPSI","FANTA LARANJA","FANTA UVA"],"CERVEJA": ["BRAHMA","SKOL","ITAIPAVA","AMSTEL"]}}

    ordersDictionary = {"NOME" : [],"PEDIDO" : [],"CODIGO" : []}

    dataBank = list()

    bankAmount = 0.0
    ordersAmount = [0,0,0,0]
    generalData = {"Products":["PIZZAS SALGADAS","PIZZAS DOCES","REFRIGERANTES","CERVEJAS"],"Amount":ordersAmount}

    create_head("Bem vindo(a) a Pizzaria da Alegria!")

    while True:
        price = 0.0
        create_menu(optionList,"Opções")
        option = int(input("Insira sua opção : "))
        if option == 1:
            print("-"*90)
            mKey = str(input("Insira 'Pizza' caso deseje pedir uma pizza ou 'Bebida' caso queira alguma bebida : ")).upper().strip()
            print("-"*90)
            if mKey == "PIZZA":
                print("-"*90)
                sKey = str(input("Insira 'Salgada' caso deseje pedir uma pizza salgada ou 'Doce' caso queira uma pizza doce : ")).upper().strip()
                print("-"*90)
                if sKey == "SALGADA":
                    price = 60.5
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    print("-"*60)
                    choiceP1 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    if choiceP1 >= 0 and choiceP1 <= len(menuDictionary[mKey][sKey]):
                        chosenProductP1 = choose_product(menuDictionary[mKey][sKey],choiceP1)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        print("-"*60)
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${:.2f}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeP1 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeP1))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductP1)
                            ordersDictionary["CODIGO"].append(rCodeP1)
                            bankAmount += price
                            ordersAmount[0] += 1
                            create_id(dataBank,chosenProductP1,userName,change,rCodeP1)
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                elif sKey == "DOCE":
                    price = 45.5
                    show_menu(menuDictionary,mKey,sKey,"Pizzas doces")
                    print("-"*60)
                    choiceP2 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    if choiceP2 >= 0 and choiceP2 <= len(menuDictionary[mKey][sKey]):
                        chosenProductP2 = choose_product(menuDictionary[mKey][sKey],choiceP2)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        print("-"*60)
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${:.2f}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeP2 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeP2))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductP2)
                            ordersDictionary["CODIGO"].append(rCodeP2)
                            bankAmount += price
                            ordersAmount[1] += 1
                            create_id(dataBank,chosenProductP2,userName,change,rCodeP2)
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                else:
                    print("Não foi possível acessar o cardápio, entrada inválida!")
            elif mKey == "BEBIDA":
                print("-"*90)
                sKey = str(input("Insira 'Refrigerante' caso deseje pedir um refrigerante ou 'Cerveja' caso queira uma cerveja : ")).upper().strip()
                print("-"*90)
                if sKey == "REFRIGERANTE":
                    price = 12.5
                    show_menu(menuDictionary,mKey,sKey,"Refrigerantes")
                    print("-"*60)
                    choiceB1 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    if choiceB1 >= 0 and choiceB1 <= len(menuDictionary[mKey][sKey]):
                        chosenProductB1 = choose_product(menuDictionary[mKey][sKey],choiceB1)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        print("-"*60)
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${:.2f}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeB1 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeB1))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductB1)
                            ordersDictionary["CODIGO"].append(rCodeB1)
                            bankAmount += price
                            ordersAmount[2] += 1
                            create_id(dataBank,chosenProductB1,userName,change,rCodeB1)
                        else:
                            print("Pagamento insuficiente!")
                    else:
                        print("Opção inválida!")
                elif sKey == "CERVEJA":
                    price = 15.25
                    show_menu(menuDictionary,mKey,sKey,"Cervejas")
                    print("-"*60)
                    choiceB2 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    if choiceB2 >= 0 and choiceB2 <= len(menuDictionary[mKey][sKey]):
                        chosenProductB2 = choose_product(menuDictionary[mKey][sKey],choiceB2)
                        userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                        print("-"*60)
                        if is_payment_valid(price,userPayValue):
                            change = make_change(price,userPayValue)
                            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${:.2f}".format(change))
                            userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                            rCodeB2 = create_random_number(ordersDictionary["CODIGO"])
                            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(rCodeB2))
                            ordersDictionary["NOME"].append(userName)
                            ordersDictionary["PEDIDO"].append(chosenProductB2)
                            ordersDictionary["CODIGO"].append(rCodeB2)
                            bankAmount += price
                            ordersAmount[3] += 1
                            create_id(dataBank,chosenProductB2,userName,change,rCodeB2)
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
            requiredCode = int(input("Insira seu código de pedido : "))
            show_data(dataBank,requiredCode)
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

    dataFrame = pd.DataFrame.from_dict(generalData)

    amountSoldMain = 0 

    for c in ordersAmount:
        amountSoldMain += c
    
    extraOption = str(input("Deseja ver o gráfico com a comparação de vendas? [S/N] : ")).upper().strip()
    if extraOption == "S" or extraOption == "SIM" or extraOption == "SS" or extraOption == "SI" or extraOption == "YES" or extraOption == "YEAH" or extraOption == "YEA" or extraOption == "YE":
        draw_graph(dataFrame,amountSoldMain)
    
    print("-=-"*20)
    print("Fim do programa!".center(60))
    print("-=-"*20)

if __name__ == "__main__":
    main()