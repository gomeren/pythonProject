import random
def display_board(board):

    divisoria = '---------'
    for i in range(3):
        print('{} | {} | {}'.format(board[i * 3], board[i * 3 + 1], board[i * 3 + 2]))
        if i < 2:
            print(divisoria)

test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(test_board)

def player_input():
    marker=str(input('Você quer ser X ou O ?'))
    while marker != 'X' and marker != 'O':
        marker=str(input('Você quer ser X ou O ?'))
    return marker

marker = player_input()
position = int(input('Insira a posição desejada'))
def place_marker(board, marker, position):
    if position <1 or position>9:
        print('So valem posições de 1 até 9, tente novamente')
        return False
    board[position-1] = marker
    display_board(board)

marker1 = place_marker(test_board, marker,position)

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
    if board[position] != ' ':
        return True
    else:
        return False

def full_board_check(board):
    for i in range(8):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    choice=input('Escolha uma posição para marcar: ')
    while space_check(board,choice) == True:
        print('Posição ja foi ocupada, escolha outra')
    return choice

def replay():
    escolha=input('Quer jogar novamente? Responda: S ou N')
    if escolha == 'S':
        return True
    return False

print(test_board)
print(test_board[1])
print(space_check(test_board, 0))



