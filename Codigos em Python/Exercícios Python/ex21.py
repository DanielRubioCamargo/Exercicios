frase = str(input("Insira uma frase qualquer : ")).strip()
print("A letra 'a' apareceu ",frase.upper().count("A")," vezes!")
print("A primeira aparição foi na posição ",frase.upper().find("A"))
print("A Ultima aparição foi na posição ",frase.upper().rfind("A"))