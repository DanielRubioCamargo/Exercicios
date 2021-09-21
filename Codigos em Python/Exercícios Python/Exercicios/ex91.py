def inverter_string(msg : str) -> str:
    return msg[::-1]


def main():
    nome = str(input("Insira seu nome : "))
    nomeInvertido = inverter_string(nome).strip().title()
    print(nomeInvertido)

if __name__ == "__main__":
    main()