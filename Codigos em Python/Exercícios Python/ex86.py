def leiaInteiro():
    while True:
        try:
            n = int(input("Insira um numero : "))
        except (ValueError,TypeError):
            print("\033[1;31mNumero ou tipo inválido!\033[m")
            continue
        except KeyboardInterrupt:
            print("O usuário não preencheu nada!")
            break
        else:
            print(n)
            break


leiaInteiro()