import pygame
from pygame.locals import *
import sys

#def top_page():

def win_close():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def main():
    pygame.init()
    display_size = (800, 600)
    screen = pygame.display.set_mode(display_size)
    pygame.display.set_caption('test')
    while True:
        screen.fill((0, 0, 0))
        pygame.display.update()
        win_close()

if __name__ == '__main__':
    main()


