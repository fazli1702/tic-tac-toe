import pygame

WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 3 or HEIGHT // 3

WHITE  = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def get_row_col(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col