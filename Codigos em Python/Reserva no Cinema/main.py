#----------------------------------------------------------------------------------------------------------
# 1-Criar um sistema de reserva de assento em uma sala de cinema para um filme específico.
# 2-INPUT(Cadastrar o nome completo de apenas uma pessoa, inserir o filme e os assentos.)
# 3-OUTPUT(Mostrar se foi concluída a reserva com sucesso, o número da sala e um código caso necessário.)
# 4-Caso já tenha assento ocupado ou não exista, e ou o filme não exista tambem, mostrar uma mensagem de erro.
# 5-Opções para mostrar as reservas feitas pelo código adquirido.
# 6-Colorir terminal para deixar mais agradável.
#----------------------------------------------------------------------------------------------------------

from funcoes import *
from time import sleep

def main():
    create_head("Welcome to the cinema!",True)
    moviesList = ["Batman","Velozes e Furiosos","Toy Story","Os incríveis","Gente Grande 2"]
    reservationList = [{"name":"Chico buarque de olinda","movie":1,"seats":[1,2,3],"code":123345}]
    optionList = ["Reserva de assentos","Exibir reserva","Excluir reserva","Sair do sistema"]
    while True:
        create_menu(optionList,"Options")
        option = int(input("Insira sua opção : "))
        movieDigit = 0
        if option == 1:
            fullName = str(input("Insira seu nome completo : "))
            print("-"*60)
            for i,c in enumerate(moviesList):
                print("{} - {}".format(i+1,c))
            print("-"*60)
            movieDigit = int(input("Insira numero do filme : "))
            if movieDigit <= 0 or movieDigit > len(moviesList):
                print("Opção de filme incorreta!")
            else:
                amountSeats = int(input("Insira a quantidade de assentos : "))
                book_seats(reservationList,fullName,movieDigit,amountSeats,moviesList)
        elif option == 2:
            showCode = int(input("Insira o código de entrada para verificar seus dados : "))
            show_reservations(reservationList,showCode,movieDigit,moviesList)
        elif option == 3:
            secureAnswer = str(input("Você tem certeza de que quer deletar sua reserva? [S/N] : ")).strip().upper()
            if secureAnswer == "S" or secureAnswer == "SIM" or secureAnswer == "SS":
                deletionCode = int(input("Insira o seu código de entrada : "))
                delete_reservation(reservationList,deletionCode)
        elif option == 4:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
        sleep(2)


if __name__ == "__main__":
    main()