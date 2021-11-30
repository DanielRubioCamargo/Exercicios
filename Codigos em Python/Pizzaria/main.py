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
    ordersAmountSP = {"PIZZAS SALGADAS" : menuDictionary["PIZZA"]["SALGADA"],"QUANTIDADE" : [0,0,0,0,0]}
    ordersAmountDP = {"PIZZAS DOCES" : menuDictionary["PIZZA"]["DOCE"],"QUANTIDADE" : [0,0,0,0]}
    ordersAmountSoda = {"REFRIGERANTES" : menuDictionary["BEBIDA"]["REFRIGERANTE"],"QUANTIDADE" : [0,0,0,0,0]}
    ordersAmountBeer = {"CERVEJAS" : menuDictionary["BEBIDA"]["CERVEJA"],"QUANTIDADE" : [0,0,0,0]}

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
                    show_menu(menuDictionary,mKey,sKey,"Pizzas salgadas")
                    price = 60.5
                    codeP1 = 0
                    print("-"*60)
                    choiceP1 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                    userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                    choice_make(menuDictionary,ordersDictionary,userName,mKey,sKey,choiceP1,price,userPayValue,codeP1,bankAmount,dataBank)
                    ordersAmount[0] += 1
                    ordersAmountSP["QUANTIDADE"][choiceP1-1] += 1
                elif sKey == "DOCE":
                    show_menu(menuDictionary,mKey,sKey,"Pizzas doces")
                    price = 45.5
                    codeP2 = 0
                    print("-"*60)
                    choiceP2 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                    userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                    choice_make(menuDictionary,ordersDictionary,userName,mKey,sKey,choiceP2,price,userPayValue,codeP2,bankAmount,dataBank)
                    ordersAmount[1] += 1
                    ordersAmountDP["QUANTIDADE"][choiceP2-1] += 1
                else:
                    print("Não foi possível acessar o cardápio, entrada inválida!")
            elif mKey == "BEBIDA":
                print("-"*90)
                sKey = str(input("Insira 'Refrigerante' caso deseje pedir um refrigerante ou 'Cerveja' caso queira uma cerveja : ")).upper().strip()
                print("-"*90)
                if sKey == "REFRIGERANTE":
                    show_menu(menuDictionary,mKey,sKey,"Refrigerantes")
                    price = 12.5
                    codeB1 = 0
                    print("-"*60)
                    choiceB1 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    chosenProductB1 = choose_product(menuDictionary[mKey][sKey],choiceB1)
                    userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                    userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                    choice_make(menuDictionary,ordersDictionary,userName,mKey,sKey,choiceB1,price,userPayValue,codeB1,bankAmount,dataBank)
                    ordersAmount[2] += 1
                    ordersAmountSoda["QUANTIDADE"][choiceB1-1] += 1
                elif sKey == "CERVEJA":
                    show_menu(menuDictionary,mKey,sKey,"Cervejas")
                    price = 15.25
                    codeB2 = 0
                    print("-"*60)
                    choiceB2 = int(input("Insira sua opção em número : "))
                    print("-"*60)
                    chosenProductB2 = choose_product(menuDictionary[mKey][sKey],choiceB2)
                    userPayValue = float(input("O total ficou R${}, quanto o(a) senhor(a) irá dar? : ".format(price)))
                    userName = str(input("Por favor insira seu nome para identificarmos : ")).strip().title()
                    choice_make(menuDictionary,ordersDictionary,userName,mKey,sKey,choiceB2,price,userPayValue,codeB2,bankAmount,dataBank)
                    ordersAmount[3] += 1
                    ordersAmountBeer["QUANTIDADE"][choiceB2-1] += 1
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

    amountSoldMain = 0 

    for c in ordersAmount:
        amountSoldMain += c

    resultList = ["Ver dados gerais","Pizzas salgadas","Pizzas doces","Refrigerantes","Cervejas","Sair"]
    while True:
        create_menu(resultList,"Resultados")
        resultOption = int(input(("Insira sua opção para ver os resultados : ")))
        if resultOption == 1:
            dataFrame1 = pd.DataFrame.from_dict(generalData)
            draw_graph(dataFrame1,"Products","Amount","Produtos","Quantidade","Vendas gerais")
        elif resultOption == 2:
            dataFrame2 = pd.DataFrame.from_dict(ordersAmountSP)
            draw_graph(dataFrame2,"PIZZAS SALGADAS","QUANTIDADE","Pizzas salgadas","Quantidade vendida","Vendas de pizzas salgadas")
        elif resultOption == 3:
            dataFrame3 = pd.DataFrame.from_dict(ordersAmountDP)
            draw_graph(dataFrame3,"PIZZAS DOCES","QUANTIDADE","Pizzas doces","Quantidade vendida","Vendas de pizzas doces")
        elif resultOption == 4:
            dataFrame4 = pd.DataFrame.from_dict(ordersAmountSoda)
            draw_graph(dataFrame4,"REFRIGERANTES","QUANTIDADE","Refrigerantes","Quantidade vendida","Vendas de refrigerantes")
        elif resultOption == 5:
            dataFrame5 = pd.DataFrame.from_dict(ordersAmountBeer)
            draw_graph(dataFrame5,"CERVEJAS","QUANTIDADE","Cervejas","Quantidade vendida","Vendas de cervejas")
        elif resultOption == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
    
    print("-=-"*20)
    print("Fim do programa!".center(60))
    print("-=-"*20)

if __name__ == "__main__":
    main()