import time

#Lista
hotelBoard = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]

#Impressão da tela para jogador visuzalizar as posições
def screen():
    print('\n' + '-' * 20)
    print('    0   1   2   3')
    print('0:  ' + hotelBoard[0][0] + ' | ' + hotelBoard[0][1] + ' | ' + hotelBoard[0][2] + ' | ' + hotelBoard[0][3])
    print('  ' + '-' * 13)
    print('1:  ' + hotelBoard[1][0] + ' | ' + hotelBoard[1][1] + ' | ' + hotelBoard[1][2] + ' | ' + hotelBoard[1][3])
    print('\n' + '-' * 20)

#Função para zerar as posições
def start_newstep():
    hotelBoard[0][0] = ' '
    hotelBoard[0][1] = ' '
    hotelBoard[0][2] = ' '
    hotelBoard[0][3] = ' '
    hotelBoard[1][0] = ' '
    hotelBoard[1][1] = ' '
    hotelBoard[1][2] = ' '
    hotelBoard[1][3] = ' '

def step1():
    start_newstep()
    print('\nFASE 01')
    print('Na fase 01, o jogador deve alocar o RATO e o GATO na seguinte matriz que representao os quartos:\n')
    #Posições pre definidas
    hotelBoard[0][0] = '*'
    hotelBoard[0][1] = '*'
    hotelBoard[0][3] = 'G'
    hotelBoard[1][0] = 'R'
    hotelBoard[1][2] = '*'
    hotelBoard[1][3] = '*'
    screen()
    print('')
    #Input de dados
    #Para inserção do elemento na posição correta é solicitado ao usuário para indicar em qual linha e coluna gostaria que o elemento ficasse.
    print('Onde você quer colocar o rato(R)?')
    lm = int(input(('Linha: ')))  #Mouse Line
    cm = int(input(('Coluna: ')))  #Mouse Column
    hotelBoard[lm][cm] = 'R'
    screen()
    print('Onde você quer colocar o gato(G)?')
    lc = int(input(('Linha: ')))  #Cat Line
    cc = int(input(('Coluna: '))) #Cat Column
    hotelBoard[lc][cc] = 'G'
    screen()
    #Estrutura Condicional para verificar as posições corretas e retornar falso ou verdadeiro
    if hotelBoard[0][2] == 'R':
        return False

    else:
        return True

def step2():
    start_newstep()
    print('\nFASE 02')
    print('Na fase 02, o jogador deve alocar: CÃO CÃO e OSSO.')
    # Posições pre definidas
    hotelBoard[0][1] = '*'
    hotelBoard[0][2] = '*'
    hotelBoard[0][3] = '*'
    hotelBoard[1][0] = '*'
    hotelBoard[1][1] = 'C'
    screen()
    print('')
    # Input de dados
    print('Onde você quer colocar o cão(C)?')
    ld = int(input(('Linha: ')))
    cd = int(input(('Coluna: ')))
    hotelBoard[ld][cd] = 'C'
    screen()
    print('Onde você quer colocar o cão(C)?')
    ld2 = int(input(('Linha: ')))
    cd2 = int(input(('Coluna: ')))
    hotelBoard[ld2][cd2] = 'C'
    screen()
    print('Onde você quer colocar o osso(O)?')
    lb = int(input(('Linha: ')))
    cb = int(input(('Coluna: ')))
    hotelBoard[lb][cb] = 'O'
    screen()
    # Estrutura Condicional para verificar as posições corretas e retornar falso ou verdadeiro
    if hotelBoard[0][0] == 'O':
        return True
    else:
        return False

def step3():
    start_newstep()
    print('\nFASE 03')
    print('Na fase 03, o jogador deve alocar: GATO RATO e OSSO.')
    # Posições pre definidas
    hotelBoard[0][1] = '*'
    hotelBoard[0][2] = '*'
    hotelBoard[0][3] = '*'
    hotelBoard[1][1] = 'G'
    hotelBoard[1][3] = '*'
    screen()
    print('')
    # Input de dados
    print('Onde você quer colocar o gato(G)?')
    lc = int(input(('Linha: ')))
    cc = int(input(('Coluna: ')))
    hotelBoard[lc][cc] = 'G'
    screen()
    print('Onde você quer colocar o rato(R)?')
    lm = int(input(('Linha: ')))
    cm = int(input(('Coluna: ')))
    hotelBoard[lm][cm] = 'R'
    screen()
    print('Onde você quer colocar o osso(O)?')
    lb = int(input(('Linha: ')))
    cb = int(input(('Coluna: ')))
    hotelBoard[lb][cb] = 'O'
    screen()
    # Estrutura Condicional para verificar as posições corretas e retornar falso ou verdadeiro
    if hotelBoard[0][0] == 'R':
        return True
    else:
        return False

def step4():
    start_newstep()
    print('\nFASE 04')
    print('Na fase 04, o jogador deve alocar: QUEIJO QUEIJO e OSSO.')
    # Posições pre definidas
    hotelBoard[0][3] = '*'
    hotelBoard[1][0] = '*'
    hotelBoard[1][1] = 'R'
    hotelBoard[1][2] = '*'
    hotelBoard[1][3] = '*'
    screen()
    print('')
    # Input de dados
    print('Onde você quer colocar o queijo(Q)?')
    lq = int(input(('Linha: ')))
    cq = int(input(('Coluna: ')))
    hotelBoard[lq][cq] = 'G'
    screen()
    print('Onde você quer colocar o queijo(Q)?')
    lq2 = int(input(('Linha: ')))
    cq2 = int(input(('Coluna: ')))
    hotelBoard[lq2][cq2] = 'R'
    screen()
    print('Onde você quer colocar o osso(O)?')
    lb = int(input(('Linha: ')))
    cb = int(input(('Coluna: ')))
    hotelBoard[lb][cb] = 'O'
    screen()
    # Estrutura Condicional para verificar as posições corretas e retornar falso ou verdadeiro
    if hotelBoard[0][1] == 'O':
        return True
    else:
        return False

#PROGRAMA PRINCIPAL

#Estrutura de repetição para controlar dinâmica do jogo
while True:

    #Estrutura condicional para testar se a função retornou verdadeira ou falsa
    if step1(): #Caso verdadeira, avança para a próxima fase
        print('\nParabéns você avançou para a próxima fase!')
        print('\n' + '-' * 60)
    else: #Caso seja falsa, como é a primeira fase o jogador retorna para o inicio
        print('Você errou. Tente a fase 01 quantas vezes quiser, mas a partir da fase 02 você terá apenas uma tentativa. Boa sorte!')
        print('\n' + '-' * 60)
        time.sleep(4)#Time sleep para esperar usuário vizualizar mensagem e em seguida reiniciar o jogo
        continue

    # Estrutura condicional para testar se a função retornou verdadeira ou falsa
    if step2():#Caso verdadeira, avança para a próxima fase
        print('\nParabéns você avançou para a próxima fase!')
        print('\n' + '-' * 60)
    else:#Caso seja falsa, jogo é encerrado
        print('Game over!')
        print('\n' + '-' * 60)
        break

    # Estrutura condicional para testar se a função retornou verdadeira ou falsa
    if step3():#Caso verdadeira, avança para a próxima fase
        print('\nParabéns você avançou para a próxima fase!')
        print('\n' + '-' * 60)
    else:#Caso seja falsa, jogo é encerrado
        print('Game over!')
        print('\n' + '-' * 60)
        break

    # Estrutura condicional para testar se a função retornou verdadeira ou falsa
    if step4():#Caso verdadeira, jogador fechou o jogo
        print('Você fechou o jogo! Parabéns!')
        print('\n' + '-' * 60)
    else:#Caso falsa, game over
        print('Quase! Game over!')
        print('\n' + '-' * 60)

    break

