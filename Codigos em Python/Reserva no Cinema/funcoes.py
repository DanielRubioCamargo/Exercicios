# Módulo

from random import randint

def create_head(title = "head_name",hasDetail = False,lineSize = 60):
    if hasDetail == False:
        print("-"*lineSize)
        print(title.center(lineSize))
        print("-"*lineSize) 
    else:
        print("-=-"*20)
        print(title.center(60))
        print("-=-"*20)


def create_menu(optionsList:list, title = "menu_name", lineSize = 60):
    print("-"*lineSize)
    print(title.center(lineSize))
    print("-"*lineSize)
    for i,c in enumerate(optionsList):
        print("{} - {}".format(i+1,c))
    print("-"*lineSize)


def book_seats(reservationsList:list, personFullName:str, movieDigit:int, amountSeats:int,moviesList:list):
    auxList = []
    verCont = 0
    verMovie = 0
    data = {"name":"","movie":0,"seats":[],"code":0}
    for i in range(amountSeats):
        number = int(input("Insira o número da {}° cadeira : ".format(i+1)))
        auxList.append(number)
        for i,c in enumerate(reservationsList):
            if c["movie"] == movieDigit and number in c["seats"]:
                verCont = 1
                break
    if verCont == 0:
        while True:
            code = randint(100000,999999)
            isValid = False
            for i,c in enumerate(reservationsList):
                if c["code"] == code:
                    isValid = False
                    break
                elif i == len(reservationsList)-1:
                    isValid = True
            if isValid == True:
                break
        data = {"name":personFullName,"movie":movieDigit,"seats":auxList,"code":code}
        reservationsList.append(data.copy())
        create_head("Sucesso!",True)
        print("Reserva criada!")
        print("Nome : {}".format(data["name"]))
        print("Filme : {}".format(moviesList[movieDigit-1]))
        print("Assentos : ",end = "")
        for i,c in enumerate(data["seats"]):
            if i == len(data["seats"])-1:
                print(c)
            else:
                print(c,end = " ")
        print("Código de entrada : {}".format(data["code"]))
        print("-=-"*20)
        data.clear()
    else:
        create_head("Erro",True)
        print("Erro ao realizar cadastro! Este assento já esta ocupado!")
        print("-=-"*20)


def show_reservations(reservationsList:list,code:int,movieChoice:int,movieList:list):
    for i in reservationsList:
        if i["code"] == code:
            create_head("Dados da reserva",True)
            print("Nome : {}".format(i["name"]))
            print("Filme : {}".format(movieList[movieChoice]))
            print("Código de entrada : {}".format(i["code"]))
            print("-=-"*20)


def delete_reservation(reservationsList:list,code:int):
    for i,c in enumerate(reservationsList):
        if c["code"] == code:
            del c
            print("Reserva deletada com sucesso!")
            break

