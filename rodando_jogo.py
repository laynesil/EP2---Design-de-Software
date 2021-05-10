from funcoes import *

baralho_do_jogador = cria_baralho()
e_invalida = True
while e_invalida:
    
    print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')
    print("Existem dois movimentos possíveis:") 
    print("1. Empilhar uma carta sobre a carta imediatamente anterior; 2. Empilhar uma carta sobre a terceira carta anterior.")
    print("Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:")
    print("As duas cartas possuem o mesmo valor ou as duas cartas possuem o mesmo naipe. Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.")

    comecar_jogo = input('Aperte [enter] para começar a jogar: ')
    if comecar_jogo != '':

        print('Digite uma entrada válida!')

    else:
        jogando = True
        e_invalida = False
        while jogando:
            print("O estado atual do baralho é: ")
            print(cartas(baralho_do_jogador))

            p_inicial = int(input('Escolha a posição inicial da carta que quer mexer: \nposição inicial: '))
            possibilidades = lista_movimentos_possiveis(baralho_do_jogador, p_inicial)
            p_final = int(input('Para onde você quer mover essa carta? \nposição final: '))
           
            if p_inicial - p_final == 1 or p_inicial - p_final == 3:            
                if lista_movimentos_possiveis(baralho_do_jogador, p_inicial) == []:
                    print('Movimento inválido. ')
                elif (lista_movimentos_possiveis(baralho_do_jogador, p_inicial) == [1] and p_inicial - p_final == 1) or (lista_movimentos_possiveis(baralho_do_jogador, p_inicial) == [3] and p_inicial - p_final == 3) or (lista_movimentos_possiveis(baralho_do_jogador, p_inicial) == [1, 3] and (p_inicial - p_final == 1) or (p_inicial - p_final ==3)):         
                    baralho_do_jogador = empilha(baralho_do_jogador, p_inicial, p_final)
                    print('Está pronto para próxima rodada? Vamos lá! ')

                else:
                    print('Movimento inválido. ')
                if possui_movimentos_possiveis(baralho_do_jogador) == False:
                    if len(baralho_do_jogador) > 1:
                        print('Você não possui mais movimentos possíveis... Você perdeu =( ')
                        jogando == False
                        
                    if len(baralho_do_jogador) == 1:
                        print('Parabéns!!!!!!!! Você ganhou o jogo!!!!!!!')
                        jogando == False
                        
            else:
                print('Movimento inválido. ')