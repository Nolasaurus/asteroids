import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill(0)
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()

        # limit to 60fps
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()