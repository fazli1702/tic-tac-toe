import pygame
from gui import *
from tictactoe import *
from ai import ai_move
import sys

def init_game(win, single_player):
    board = init_board()
    turn = get_turn(board)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_row_col(x, y)
                if board[row][col] == '':
                    select(board, row, col)
                    update(board, win)

                    if has_won(board, turn):
                        draw_end(f'{turn} WINS', win)
                        init_game(win, single_player)

                    if is_full(board):
                        draw_end('TIE', win)
                        init_game(win, single_player)

                    turn = get_opposite_turn(turn)

                    if single_player:
                        pygame.time.delay(200)
                        ai_move(board)
                        update(board, win)

                        if has_won(board, turn):
                            draw_end(f'{turn} WINS', win)
                            init_game(win, single_player)

                        if is_full(board):
                            draw_end('TIE', win)
                            init_game(win, single_player)

        update(board, win)