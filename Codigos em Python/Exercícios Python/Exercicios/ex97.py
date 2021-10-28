def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)

def main():
    print(fatorial(5))

if __name__ == "__main__":
    main()