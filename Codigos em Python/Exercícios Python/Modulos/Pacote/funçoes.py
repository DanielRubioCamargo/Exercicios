def aumentar(valor,aumento):
    novoValor = valor + (valor*(aumento/100))
    return novoValor

def diminuir(valor,diminuicao):
    novoValor = valor - (valor*(diminuicao/100))
    return novoValor
    
if __name__ == "__main__":
    print(__name__)