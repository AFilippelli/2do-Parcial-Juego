import pygame
import sys
from menu import Menu
from constantes import *


pygame.display.set_caption("Dark Conquer") #nombre del juego
def main():
    pygame.init()

    menu = Menu(1300,800)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        menu.main_menu()

        pygame.display.flip()


if __name__ == '__main__':
    main()
