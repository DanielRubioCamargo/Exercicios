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
# * 'KEYS' : PIZZA, SALGADA, DOCE, BEBIDA, REFRIGERANTE, CERVEJA
#------------------------------------------------------------------------------------------------------------

from funcoes import *

optionList = ["Realizar um pedido","Dar um feedback","Fazer uma doação","Sair do sistema"]

menuDictionary = {"PIZZA" : {"SALGADA" : ["FRANGO COM CATUPIRY","ATUM","PORTUGUESA","CALABRESA","QUEIJO"],"DOCE" : ["NUTELLA","DOCE DE LEITE","MORANGO COM CHOCOLATE"]}, "BEBIDA" : {"REFRIGERANTE" : ["GUARANÁ","COCA-COLA","PEPSI","FANTA LARANJA","FANTA UVA"],"CERVEJA": ["BRAHMA","SKOL","ITAIPAVA","AMSTEL"]}}

create_head("Bem vindo(a) a Pizzaria da Alegria!")

def main():
    while True:
        create_menu(optionList,"Opções")
        option = int(input("Insira sua opção : "))
        if option == 1:
            mKey = str(input("Insira 'Pizza' caso deseje pedir uma pizza ou 'Bebida' caso queira alguma bebida : ")).upper().strip()
            if mKey == "PIZZA":
                sKey = str(input("Insira 'Salgada' caso deseje pedir uma pizza salgada ou 'Doce' caso queira uma pizza doce : ")).upper().strip()
                show_menu(menuDictionary,mKey,sKey)
            elif mKey == "BEBIDA":
                sKey = str(input("Insira 'Refrigerante' caso deseje pedir um refrigerante ou 'Cerveja' caso queira uma cerveja : ")).upper().strip()
                show_menu(menuDictionary,mKey,sKey)
            else:
                print("Não foi possível acessar o cardápio, entrada inválida!")
            
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()