import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    game_loop()

def game_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    while True:
        screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill(0)
        pygame.display.flip()




if __name__ == "__main__":
    main()