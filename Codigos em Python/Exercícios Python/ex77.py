listaGols = list()
jogador = dict()
jogadores = list()
resp = 0
while resp != -1:
    nome = str(input("Insira seu nome : "))
    qtdPartidas = int(input("Quantidade de partidas : "))
    for i in range(0,qtdPartidas,1):
        listaGols.append(int(input("Quantidade de gols na partida {} : ".format(i+1))))
    jogador = {"nome":nome,"partidas":qtdPartidas,"listaDeGols":listaGols[:]}
    jogadores.append(jogador.copy())
    jogador.clear()
    listaGols.clear()
    resp = int(input("Digite qualquer coisa menos -1 para repetir o programa : "))
resposta2 = str(input("Qual jogador você escolhe para ver os dados : "))
for i, c in enumerate(jogadores):
    if(c["nome"] == resposta2):
        print("{} jogou {} partidas!".format(c["nome"],c["partidas"]))
        resposta3 = int(input("Qual jogo você quer saber a quantidade de gols : "))
        for i,c in enumerate(c["listaDeGols"]):
            if(i+1 == resposta3):
                print(c)