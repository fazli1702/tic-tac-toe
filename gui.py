import pygame
from constant import *
import sys

def menu(win):
    while True:
        win.fill(WHITE)

        size = 75
        draw_text('1 PLAYER', BLUE, WIDTH//4, HEIGHT//2, size, win)
        draw_text('2 PLAYER', BLUE, int(WIDTH*(3/4)), HEIGHT//2, size, win)
        pygame.draw.line(win, BLACK, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x < WIDTH // 2:
                    return True
                return False

        pygame.display.update()

def draw_text(text, colour, x, y, size, win):
    '''helper function to draw text onto window'''
    font = pygame.font.SysFont(None, size)
    text = font.render(text, True, colour)
    text_rect = text.get_rect(center=(x, y))
    win.blit(text, text_rect)

def draw_end(text, win):
    '''draw text to show WIN or TIE when the game ends'''
    # draw white background to cover board (able to see text clearly)
    pygame.draw.rect(win, WHITE, (0, SQUARE_SIZE, WIDTH, SQUARE_SIZE))

    # render text
    draw_text(text, RED, WIDTH//2, HEIGHT//2, 200, win)
    pygame.display.update()
    pygame.time.delay(400)  # delay 400ms to see text on window

def draw_grid(win):
    '''draw checkerboard pattern on window'''
    win.fill(WHITE)
    thickness = 5
    # draw col lines
    for i in range(1, 3):
        pygame.draw.line(win, BLACK, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), thickness)
    # draw col lines
    for i in range(1, 3):
        pygame.draw.line(win, BLACK, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), thickness)

def draw_board(board, win):
    '''draw "O" & "X" on window'''
    k = SQUARE_SIZE // 2 # constant
    for i in range(3):
        for j in range(3):
            text = board[i][j]
            x = (j * SQUARE_SIZE) + k
            y = (i * SQUARE_SIZE) + k
            draw_text(text, BLACK, x, y, 200, win)

def update(board, win):
    draw_grid(win)
    draw_board(board, win)
    pygame.display.update()


