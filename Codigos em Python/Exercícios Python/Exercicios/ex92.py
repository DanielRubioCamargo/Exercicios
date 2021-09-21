def achar(msg : str,caracter : str) -> int:
    if caracter in msg:
        for i,c in enumerate(msg):
            if c == caracter:
                return i
                break
    return -1

def main():
    while True:
        texto = str(input("Insira um texto qualquer : "))
        print(achar(texto,"a"))

if __name__ == "__main__":
    main()