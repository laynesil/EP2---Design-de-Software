from funcoes import *

print('''
Paciência Acordeão 
================== 

Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

Existem apenas dois movimentos possíveis: 

1. Empilhar uma carta sobre a carta imediatamente anterior; 
2. Empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

1. As duas cartas possuem o mesmo valor ou 
2. As duas cartas possuem o mesmo naipe. 

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

''')
comecar_jogo = input('Aperte [enter] para começar a jogar: ')

baralho_do_jogador = cria_baralho()
i = 1
for carta in baralho_do_jogador:
    print(f"\033[34m {i}. {cor(carta)} ")
     
    i += 1


e_invalida = True
while e_invalida:
    while len(baralho_do_jogador) > 1 and possui_movimentos_possiveis(baralho_do_jogador) == True:

                carta = int(input('Escolha o número de uma carta para jogar de {0} a {1}:'.format(1, len(baralho_do_jogador))))

                while carta > len(baralho_do_jogador) or carta <= 0:
                    print('Carta inválida!')
                    carta = int(input('Escolha o número de uma carta para jogar de {0} a {1}:'.format(1, len(baralho_do_jogador))))
                
            
                possibilidade = lista_movimentos_possiveis(baralho_do_jogador,(carta - 1))
                

                while possibilidade == []:
                    vazia = int(input('Digite uma entrada válida!'))
                    iv = vazia - 1
                    possibilidade = lista_movimentos_possiveis(baralho_do_jogador,iv)
                
                if possibilidade == [1] :
                    for cada, car in enumerate(empilha(baralho_do_jogador, (carta - 1) , (carta - 1) - 1)):
                        arg = cada + 1
                        print(('{0}'.format(arg))+ ' ' + cor(car))
                    
                
                if possibilidade == [3]:
                    for cada, car in enumerate(empilha(baralho_do_jogador, (carta - 1) , (carta - 1) - 3)):
                        arg = cada + 1
                        print(('{0}'.format(arg))+ ' ' + cor(car))
                    
                
                if possibilidade == [1,3]:
                    mov = True
                    while mov:
                        empilha1 = int(input('Escolha a carta que deseja empilhar ({0} ou {1}):'.format((carta - 1), (carta - 1) - 2)))
                        ie = empilha1 - 1

                        if ie == (carta - 1) - 3 or ie == (carta - 1) - 1:
                            for cada, car in enumerate(empilha(baralho_do_jogador, (carta - 1) , ie)):
                                arg = cada + 1
                                print(('{0}'.format(arg))+ ' ' + cor(car))
                            mov = False
                        else:
                            print('Digite uma entrada válida!')
                            mov = True
                    
                        if len(baralho_do_jogador) == 1 and possui_movimentos_possiveis(baralho_do_jogador) != True:
                            print ('Fim do jogo. Obrigado por jogar!')
                        jogar_dnv = input('Você deseja jogar novamente ?(s/n) ')
                        if jogar_dnv == 's':
                            jogando = True
                            for cada, car in enumerate(baralho_do_jogador):
                                arg = cada + 1
                                print(('{0}'.format(arg))+ ' ' + cor(car))
                        else:
                            jogando = False
