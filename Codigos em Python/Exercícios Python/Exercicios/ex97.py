def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero - 1)

def main():
    print(pot(5,2))

def pot(number,exp):
    if exp == 0:
        return 1
    return number * pot(number,exp-1)

if __name__ == "__main__":
    main()