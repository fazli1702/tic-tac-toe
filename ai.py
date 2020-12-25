from tictactoe import *

def ai_move(board):
    best_score = -float('inf')
    turn = get_turn(board)
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = turn
                score = minimax(board, 0, False, turn)
                board[row][col] = '' # undo move
                if score > best_score:
                    best_score = score
                    move = row, col
    row, col = move
    board[row][col] = turn

def minimax(board, depth, isMaximizing, turn):
    state = get_state(board)
    if state != None:
        if state == turn:
            return +10 - depth
        elif state == 'TIE':
            return 0
        else:
            return -10 + depth

    if isMaximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = turn
                    score = minimax(board, depth + 1, False, turn)
                    board[row][col] = ''
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = get_opposite_turn(turn)
                    score = minimax(board, depth + 1, True, turn)
                    board[row][col] = ''
                    best_score = min(score, best_score)
        return best_score
