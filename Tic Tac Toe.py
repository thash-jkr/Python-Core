import random


def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    check = False

    for i in [1, 2, 3]:
        if board[i] == board[i + 3] == board[i + 6] == mark:
            check = True

    for i in [1, 4, 7]:
        if board[i] == board[i + 1] == board[i + 2] == mark:
            check = True

    if board[3] == board[5] == board[7] == mark or board[1] == board[5] == board[9] == mark:
        check = True

    return check


def choose_first():
    choice = random.randint(0, 1)
    if choice == 0:
        print("Player 1 can go first")
        return 0
    else:
        print("Player 2 can go first")
        return 1


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in range(1, 10) and not space_check(board, position):
        position = int(input('Enter your next position (1-9): '))

    return position


def replay():
    replay0 = input('Are you ready to play again? (Y or N): ').upper()
    if replay0 == 'Y':
        return True
    elif replay0 == 'N':
        return False


def ready():
    red = input('Are you ready? (Y or N): ').upper()
    if red == 'Y':
        return True
    else:
        return False


while True:
    print('Welcome to Tic-Tac-Toe')
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    display_board(game_board)
    game_on = ready()
    player_1 = player_input()[0]
    choice0 = choose_first()
    marker0 = " "

    while game_on:

        if choice0 == 0:
            marker0 = player_1
        elif choice0 == 1:
            if player_1 == 'X':
                marker0 = 'O'
            elif player_1 == 'O':
                marker0 = 'X'

        position0 = player_choice(game_board)
        place_marker(game_board, marker0, position0)
        print('\n' * 100)
        display_board(game_board)

        if win_check(game_board, 'X'):
            if player_1 == 'X':
                print('Player 1 has won the game')
                print('\n' * 3)
                break
            else:
                print('Player 2 has won the game')
                print('\n' * 3)
                break
        elif win_check(game_board, 'O'):
            if player_1 == 'X':
                print('Player 2 has won the game')
                print('\n' * 3)
                break
            else:
                print('Player 1 has won the game')
                print('\n' * 3)
                break
        elif full_board_check(game_board):
            print('Oooooooooooooooooooooooooooppppppppppppppppsssssssssssssssssss')
            print('Match is Drawn')
            print('\n' * 3)
            break
        else:
            if choice0 == 1:
                choice0 = 0
            elif choice0 == 0:
                choice0 = 1

    if not replay():
        break
