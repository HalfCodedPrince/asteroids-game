import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    asteroid_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group)
    AsteroidField.containers = (updatable_group)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    game_loop(updatable_group, drawable_group, asteroid_group, player)


def game_loop(updatable, drawable, asteroid_group, player):
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        check_collision(asteroid_group, player)
        pygame.Surface.fill(screen, color="black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        
def check_collision(asteroid_group, player):
    for asteroid in asteroid_group:
        if asteroid.is_colliding(player):
            sys.exit("Game over!")


if __name__ == "__main__":
    main()
