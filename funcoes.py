import random
# faz como lista as cartas de um baralho e embaralha
def cria_baralho():
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['♦', '♣', '♥', '♠']
    baralho = []
    for i in faces:
        for k in naipes:
            baralho.append(i+k)
    random.shuffle(baralho)      
    return baralho
print(cria_baralho())

#função para descobrir qual o naipe da carta
def extrai_naipe(carta):
    naipe = carta[-1]
    return naipe 

#função para descobrir qual valor da carta
def extrai_valor(carta):
    valor = carta[:-1]
    return valor

#função para definir quais sao os possiveis movimentos no jogo
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

#funcao para empilhar as cartas em seus devidos lugares
def empilha(baralho, i_o, i_d):
    remove_carta = baralho.pop(i_o)
    baralho[i_d] = remove_carta
    return baralho

#funcao que verifica se há movimentos ainda a serem feitos
def possui_movimentos_possiveis(baralho):
    for e in range(len(baralho)):
        if lista_movimentos_possiveis(baralho, e) == [1] or lista_movimentos_possiveis(baralho, e) == [3] or lista_movimentos_possiveis(baralho, e) == [1, 3]:
            return True
    return False
    
# função para colocar as cartas em coluna ao lado do numero para melhor visualização do baralho
def cartas(baralho):
    cartas = ''
    for i in baralho:
        cartas += '{}. {} \n'.format(baralho.index(i)+1, i)
    return cartas
    