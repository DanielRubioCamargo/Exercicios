import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

gradesDF = pd.read_excel("Codigos em Python\\Finale\\Notas Python.xlsx")

xValues = []
yValues = []

while True:
    print("1 -> Notas 1\n2 -> Notas 2\n3 -> Medias\n4 -> Sair")
    option = int(input("Insira sua opção : "))
    if option == 1:
        yValues = gradesDF["Nota 1"]
    elif option == 2:
        yValues = gradesDF["Nota 2"]
    elif option == 3:
        yValues = gradesDF["Media"]
    elif option == 4:
        break
    else:
        print("Inválido")
        continue
    title = str(input("Insira um titulo : "))
    xValues = gradesDF["Nome"]
    plt.bar(xValues,yValues)
    plt.title(title)
    plt.show()

    
