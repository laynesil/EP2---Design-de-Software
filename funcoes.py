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

def lista_movimentos_possiveis(baralho, indice):
    if indice == 0:
        return []
    if indice > 0 and indice < 3:
        if (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1])) or (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1])):
            return [1] 
        else:
            return []
    if indice >= 3:
        mesmo_valor_1 = (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-1]))
        mesmo_valor_3 = (extrai_valor(baralho[indice]) == extrai_valor(baralho[indice-3]))
        mesmo_naipe_1 = (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-1]))
        mesmo_naipe_3 = (extrai_naipe(baralho[indice]) == extrai_naipe(baralho[indice-3]))

        if (mesmo_valor_1 or mesmo_naipe_1 ) and ( mesmo_valor_3 or mesmo_naipe_3 ):
            return [1, 3]
        elif mesmo_valor_1 or mesmo_naipe_1:
            return [1]
        elif mesmo_valor_3 or mesmo_naipe_3:
            return [3]
        
        else:
            return []