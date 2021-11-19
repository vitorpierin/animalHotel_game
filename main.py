import os

hotelBoard = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]
def screen():

    print('    0   1   2   3')
    print('0:  ' + hotelBoard[0][0] + ' | ' + hotelBoard[0][1] + ' | ' + hotelBoard[0][2] + ' | ' + hotelBoard[0][3])
    print('  ' + '-' * 13)
    print('1:  ' + hotelBoard[1][0] + ' | ' + hotelBoard[1][1] + ' | ' + hotelBoard[1][2] + ' | ' + hotelBoard[1][3])

def start_newstep():
    hotelBoard[0][0] = ' '
    hotelBoard[0][1] = ' '
    hotelBoard[0][2] = ' '
    hotelBoard[0][3] = ' '
    hotelBoard[1][0] = ' '
    hotelBoard[1][1] = ' '
    hotelBoard[1][2] = ' '
    hotelBoard[1][3] = ' '


while True:
    print('\nFASE 01')
    print('Na fase 01, o jogador deve alocar o RATO e o GATO na seguinte matriz que representao os quartos:\n')
    hotelBoard[0][0] = '*'
    hotelBoard[0][1] = '*'
    hotelBoard[0][3] = 'G'
    hotelBoard[1][0] = 'R'
    hotelBoard[1][2] = '*'
    hotelBoard[1][3] = '*'
    screen()
    while True:
        print('')
        print('Onde você quer colocar o rato(R)?')
        lm = int(input(('Linha: '))) #Mouse Line
        cm = int(input(('Coluna: ')))#Mouse Column
        hotelBoard[lm][cm] = 'R'
        print('Onde você quer colocar o gato(G)?')
        lc = int(input(('Linha: ')))
        cc = int(input(('Coluna: ')))
        hotelBoard[lc][cc] = 'G'
        screen()
        if lm == 0:
            print('Game Over!')
            break
        elif lm == 1:
            break
        else:
            print('Coluna e/ou linha inválida. Tente outra vez!')
            continue
    print('\nParabéns você avançou para a próxima fase!')
    print('\n' + '-' * 60)
    start_newstep()
    print('\nFASE 02')
    print('Na fase 02, o jogador deve alocar: CÃO CÃO e OSSO.')
    hotelBoard[0][1] = '*'
    hotelBoard[0][2] = '*'
    hotelBoard[0][3] = '*'
    hotelBoard[1][0] = '*'
    screen()
    print('')
    print('Onde você quer colocar o cão(C)?')
    ld = int(input(('Linha: ')))
    cd = int(input(('Coluna: ')))
    hotelBoard[ld][cd] = 'C'
    print('Onde você quer colocar o cão(C)?')
    ld2 = int(input(('Linha: ')))
    cd2 = int(input(('Coluna: ')))
    hotelBoard[ld2][cd2] = 'C'
    print('Onde você quer colocar o osso(O)?')
    lo = int(input(('Linha: ')))
    co = int(input(('Coluna: ')))
    hotelBoard[lo][co] = 'O'
    screen()
    if hotelBoard[0][0] == 'O':
        print('\nParabéns você avançou para a próxima fase!')
    elif hotelBoard[0][0] == 'C' and hotelBoard[1][2] == ' ':
        print('\nParabéns você avançou para a próxima fase!')
    else:
        print('Game over!')
        break
    print('\n' + '-' * 60)
    start_newstep()
    print('\nFASE 03')
    print('Na fase 03, o jogador deve alocar: GATO RATO e OSSO.')
    hotelBoard[0][1] = '*'
    hotelBoard[0][2] = '*'
    hotelBoard[0][3] = '*'
    hotelBoard[1][3] = '*'
    screen()
    print('')
    print('Onde você quer colocar o gato(G)?')
    lc = int(input(('Linha: ')))
    cc = int(input(('Coluna: ')))
    hotelBoard[lc][cc] = 'G'
    print('Onde você quer colocar o rato(R)?')
    lm = int(input(('Linha: ')))
    cm = int(input(('Coluna: ')))
    hotelBoard[lm][cm] = 'R'
    print('Onde você quer colocar o osso(O)?')
    lo = int(input(('Linha: ')))
    co = int(input(('Coluna: ')))
    hotelBoard[lo][co] = 'O'
    screen()
    if hotelBoard[0][0] == 'R' or hotelBoard[0][0] == 'G':
        print('\nParabéns você avançou para a próxima fase!')
    elif hotelBoard[0][0] == 'O' and hotelBoard[1][1] != ' ':
        print('Game over!')
        break
    print('\n' + '-' * 60)
    start_newstep()
    print('\nFASE 04')
    print('Na fase 04, o jogador deve alocar: QUEIJO QUEIJO e OSSO.')
    hotelBoard[0][3] = '*'
    hotelBoard[1][0] = '*'
    hotelBoard[1][2] = '*'
    hotelBoard[1][3] = '*'
    screen()
    print('')
    break

        #if mouse == 1 or 2 or 7 or 8:
         #   print('Quarto ocupado! Tente novamente!')
          #  continue
        #elif mouse == 3:
           # board[0][2] = 'R'
        #elif mouse == 4:
            #board[0][3] = 'R'
       # elif mouse == 5:
            #board[1][0] = 'R'
        #elif mouse == 6:
            #board[1][1] = 'R'
