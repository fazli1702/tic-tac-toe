def init_board():
    return [['' for _ in range(3)] for _ in range(3)]

def select(board, row, col):
    board[row][col] = get_turn(board)

def print_board(board):
    for i, row in enumerate(board):
        print(' | '.join(list(map(lambda x: x if x != '' else ' ', row))))
        if i != 2:
            print('-' * 9)
    print('=' * 9)

def is_full(board):
    for row in board:
        for col in row:
            if col == '':
                return False
    return True

def is_empty(board):
    for row in board:
        for col in row:
            if col != '':
                return False
    return True

def get_turn(board):
    if is_empty(board):
        return 'O'
    
    O, X = 0, 0
    for row in board:
        for col in row:
            if col == 'O':
                O += 1
            if col == 'X':
                X += 1
    if O == X:
        return 'O'
    else:
        return 'X'

def get_opposite_turn(turn):
    return 'O' if turn == 'X' else 'X'

def has_won(board, turn):
    # check row
    for row in board:
        win = True
        for col in row:
            if col != turn:
                win = False
        if win:
            return True

    # check col
    for col in range(3):
        win = True
        for row in range(3):
            if board[row][col] != turn:
                win = False
        if win:
            return True

        # check diagonal
        win = True
        for i in range(3):
            if board[i][i] != turn:
                win = False
        if win:
            return True

        win = True
        for row in range(3):
            col = 2 - row
            if board[row][col] != turn:
                win = False
        if win:
            return True

    return False

def get_state(board):
    if has_won(board, 'O'):
        return 'O'
    if has_won(board, 'X'):
        return 'X'
    if is_full(board):
        return 'TIE'



