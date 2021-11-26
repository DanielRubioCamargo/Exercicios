from random import randint
import random

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