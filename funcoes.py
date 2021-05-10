def cria_baralho():
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['♦', '♣', '♥', '♠']
    baralho = []
    for i in faces:
        for k in naipes:
            baralho.append(i+k)
    return baralho
print(cria_baralho())

def extrai_naipe(carta):
    naipe = carta[-1]
    return naipe 

def extrai_valor(carta):
    valor = carta[:-1]
    return valor