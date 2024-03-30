import random
def display_board(board):

    divisoria = '---------'
    for i in range(3):
        print('{} | {} | {}'.format(board[i * 3], board[i * 3 + 1], board[i * 3 + 2]))
        if i < 2:
            print(divisoria)

def player_input():
    marker=input('Você quer ser X ou O ? ')
    while marker != 'X' and marker != 'O':
        marker=input('Você quer ser X ou O ? ')
    return marker


def place_marker(board, marker, position):
    board[position-1] = marker
    display_board(board)

def win_check(board,mark):
    possibilidades=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for test in possibilidades:
        if board[test[0]] == board[test[1]] == board[test[2]] == mark:
            return True
    return False

def choose_first():
    escolha=random.randint(1,2)
    if escolha == 1:
        print('Jogador 1 deve começar jogando')
    else:
        print('Jogador 2 deve começar jogando')

def space_check(board, position):
    if board[position-1] != ' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in range(9):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    choice = int(input('Escolha uma posição para marcar: '))
    while choice>9 or choice<1:
        choice= int(input('O número deve estar na faixa entre 1 e 9. Escolha outro: '))
    while space_check(board, choice):
        choice = int(input('Posição ja foi ocupada, escolha outra: '))
        while choice>9 or choice<1:
            choice = int(input('O número deve estar na faixa entre 1 e 9. Escolha outro: '))
    return choice

def replay():
    escolha=input('Quer jogar novamente? Responda: S ou N :')
    if escolha == 'S':
        return True
    return False


def jogo_da_velha():
    vontade = True
    while vontade:
        #Insere o tabuleiro padrão vazio e informa aos jogadores que o jogo começará.
        tabuleiro=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        input('\n----------------\nO Jogo da velha será iniciado\nDecida quem será o jogador 1 e o jogador 2\nPressione Enter para prosseguir\n')

        #Define quem jogará primeiro.
        choose_first()

        #O Jogador sorteado escolhe um Simbolo para si.
        marker_1=player_input()
        input('Pressione Enter para Continuar')
        #Define o simbolo do jogador não sorteado.
        if marker_1 == 'X':
            marker_2='O'
        else:
            marker_2='X'
        print('\nPróximo jogador,seu marcador é -> {} <-'.format(marker_2))
        input('Pressione Enter para confirmar')

        print('\nO Jogo irá começar, favor seguir a sequencia correta de jogadas começando pelo jogador sorteado')
        input('Pressione Enter para confirmar o início do jogo')
        while full_board_check(tabuleiro) == False:
            print('\nPrimeiro jogador sorteado: ')
            position1 = player_choice(tabuleiro)
            place_marker(tabuleiro,marker_1,position1)
            if win_check(tabuleiro,marker_1) == True:
                input('VOCÊ GANHOU! Pressione enter para continuar')
                break
            if full_board_check(tabuleiro) == True:
                break
            input('\nPressione Enter para proxima jogada')
            print('\nSegundo jogador sorteado: ')
            position2 = player_choice(tabuleiro)
            place_marker(tabuleiro, marker_2, position2)
            if win_check(tabuleiro, marker_2) == True:
                input('VOCÊ GANHOU! Pressione enter para continuar')
                break
            input('\nPressione Enter para proxima jogada')
        vontade = replay()

jogo_da_velha()







