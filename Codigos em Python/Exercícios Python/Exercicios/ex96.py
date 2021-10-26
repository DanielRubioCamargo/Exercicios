def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)

def potencia(numero,expoente):
    if expoente == 0:
        return 1
    return numero * potencia(numero,expoente-1)

def main():
    pass

if __name__ == "__main__":
    main()