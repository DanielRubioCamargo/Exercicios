def main():
    n = int(input("Insira a quantidade de alunos : "))
    alunos = list()
    dados = {}
    for i in range(n):
        nome = str(input("Insira seu nome : "))
        n1 = float(input("Insira a nota 1 : "))
        n2 = float(input("Insira a nota 2 : "))
        n3 = float(input("Insira a nota 3 : "))
        media = (n1+n2+n3)/3
        dados = {"nome":nome,"nota1":n1,"nota2":n2,"nota3":n3,"media":media}
        alunos.append(dados.copy())
        dados.clear()
    alunoEscolhido = str(input("Qual aluno vc quer consultar a media? : "))
    for c in alunos:
        if c["nome"] == alunoEscolhido:
            print("{:.2f}".format(c["media"]))

if __name__ == "__main__":
    main()