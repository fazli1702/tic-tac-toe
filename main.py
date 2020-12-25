from constant import WIDTH, HEIGHT
from gui import menu
from game import init_game
import pygame


pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def main():
    single_player = menu(WIN)
    print(single_player)
    while True:
        init_game(WIN, single_player)


if __name__ == "__main__":
    main()