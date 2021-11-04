#----------------------------------------------------------------------------------------------------------
# 1-Criar um sistema de reserva de assento em uma sala de cinema para um filme específico.
# 2-INPUT(Cadastrar o nome completo de apenas uma pessoa, inserir o filme e os assentos.)
# 3-OUTPUT(Mostrar se foi concluída a reserva com sucesso, o número da sala e um código caso necessário.)
# 4-Caso já tenha assento ocupado ou não exista, e ou o filme não exista tambem, mostrar uma mensagem de erro.
# 5-Opções para mostrar as reservas feitas pelo código adquirido.
# 6-Colorir terminal para deixar mais agradável.
# 7*-KEYS utilizadas no dicionario : 'name', 'movie', 'seats' e 'code'.
#----------------------------------------------------------------------------------------------------------
# TO-DO
# Colocar uma mensagem quando não foi encontrado uma reserva para exibir ou cancelar.
# Implementar uma função própria para um 'funcionario' manipular o cartaz de exibição de filmes.
# Resolver bugs.
#-----------------------------------------------------------------------------------------------------------

from funcoes import *
from time import sleep

def main():
    create_head("        \033[1;35mBem vindo ao cinema!\033[m",True)
    moviesList = ["Batman","Velozes e Furiosos","Toy Story 4","Os incríveis","Gente Grande 2"]
    reservationList = [{"name":"Chico buarque de olinda","movie":1,"seats":[1,2,3],"code":123345}]
    optionList = ["Reserva de assentos","Exibir reserva","Cancelar reserva","Sair do sistema"]
    while True:
        create_menu(optionList,"Opções")
        movieDigit = 0
        try:
            option = int(input("Insira sua opção : "))
        except:
            print("\033[1;31mDado inserido está incorreto (tipo ou valor)!\033[m")
        else:
            if option == 1:
                fullName = str(input("Insira seu nome completo : ")).strip().title()
                print("-"*60)
                for i,c in enumerate(moviesList):
                    print("\033[1;36m{}\033[m - \033[1m{}\033[m".format(i+1,c))
                print("-"*60)
                movieDigit = int(input("Insira numero do filme : "))
                if movieDigit <= 0 or movieDigit > len(moviesList):
                    print("\033[1;31mOpção de filme incorreta!\033[m")
                else:
                    amountSeats = int(input("Insira a quantidade de assentos : "))
                    book_seats(reservationList,fullName,movieDigit,amountSeats,moviesList)
            elif option == 2:
                showCode = int(input("Insira o código de entrada para verificar seus dados : "))
                show_reservations(reservationList,showCode,movieDigit,moviesList)
            elif option == 3:
                secureAnswer = str(input("\033[1;33mVocê tem certeza de que quer deletar sua reserva? [S/N] : \033[m")).strip().upper()
                if secureAnswer == "S" or secureAnswer == "SIM" or secureAnswer == "SS":
                    deletionCode = int(input("Insira o seu código de entrada : "))
                    delete_reservation(reservationList,deletionCode)
            elif option == 4:
                print("\033[1;33mSaindo do sistema...\033[m")
                break
            else:
                print("\033[1;31mOpção inválida!\033[m")
            sleep(0.75)


if __name__ == "__main__":
    main()