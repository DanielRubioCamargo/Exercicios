from random import randint
import random
import matplotlib.pyplot as plt

def create_head(title = "título",lineSize = 60):
    print("-"*lineSize)
    print(title.center(lineSize))
    print("-"*lineSize)


def create_menu(lst : list, title = "menu",lineSize = 60):
    print("-"*lineSize)
    print(title.center(lineSize))
    print("-"*lineSize)
    for i,c in enumerate(lst):
        print("{} - {}".format(i+1,c))
    print("-"*lineSize)


def show_menu(prodDict : dict,mainKey : str,subKey : str,description : str):
    create_head("Cardápio")
    create_head("{}".format(description.title()))
    for i,c in enumerate(prodDict[mainKey][subKey]):
        print("{} -> {}".format(i+1,c))
    

def choose_product(productList : list,chosenOption : int):
    correctOption = chosenOption - 1
    for i,c in enumerate(productList):
        if i == correctOption:
            return c
            break
        elif i == len(productList) - 1:
            return ""

def is_payment_valid(productValue : float,userValue : float) -> bool:
    if userValue >= productValue:
        return True
    return False


def make_change(productValue : float,userValue : float) -> float:
    return userValue - productValue


def create_random_number(lst : list):
    while True:
        randomNumber = randint(1000,9999)
        if randomNumber in lst:
            continue
        else:
            return randomNumber


def create_id(masterLst : list, order : str,name : str, changeValue : float,code : int):
    dataLst = list()
    dataLst.append(name)
    dataLst.append(order)
    dataLst.append(changeValue)
    dataLst.append(code)
    masterLst.append(dataLst[:])
    dataLst.clear()


def show_data(lst:list,code:int):  
    for i,c in enumerate(lst):
        if c[3] == code:
            create_head("Informações do pedido")
            print("Nome : {}".format(c[0]))
            print("Pedido : {}".format(c[1]))
            print("Valor do troco : R${:.2f}".format(c[2]))
            print("Código : {}".format(c[3]))
            print("-"*60)
            break
        elif i == len(lst) - 1:
            print("Não foi encontrado nenhum pedido com o código {}!".format(code))


def draw_graph(dataFrame,xA,yA,x,y,customTitle):
    plt.figure(figsize=(12,5))
    plt.bar(dataFrame[xA],dataFrame[yA],color = "red")
    plt.title(customTitle)
    plt.xlabel = x
    plt.ylabel = y
    plt.grid()
    plt.show()


def choice_make(menuDictionary : dict,ordersDictionary : dict,userName,mKey : str,sKey : str, choice,price : float, userPayValue : float,code : int,bankAmount, dataBank):
    print("-"*60)
    if choice >= 0 and choice <= len(menuDictionary[mKey][sKey]):
        chosenProductP1 = choose_product(menuDictionary[mKey][sKey],choice)
        if is_payment_valid(price,userPayValue):
            change = make_change(price,userPayValue)
            print("Sucesso! Seu pagamento foi efetuado!\nTotal do troco : R${:.2f}".format(change))
            code = create_random_number(ordersDictionary["CODIGO"])
            print("Sucesso! Seu código de pedido foi gerado. Código : {}".format(code))
            ordersDictionary["NOME"].append(userName)
            ordersDictionary["PEDIDO"].append(chosenProductP1)
            ordersDictionary["CODIGO"].append(code)
            bankAmount += price
            create_id(dataBank,chosenProductP1,userName,change,code)
        else:
            print("Pagamento insuficiente!")
    else:
        print("Opção inválida!")