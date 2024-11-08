import pygame
from constants import *
from player import *
from asteroidfield import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    Player.containers = (updatable, drawable)

    Shot.containers = (shot, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        dt = (clock.tick(60)) / 1000

        pygame.Surface.fill(screen, "black")
        
        for obj in drawable:
            obj.draw(screen)
        
        for updates in updatable:
            updates.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid) == True:
                print("Game over!")
                return pygame.QUIT

        for asteroid in asteroids:
            for bullet in shot:
                if bullet.collisions(asteroid) == True:
                    bullet.kill()
                    asteroid.split()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()