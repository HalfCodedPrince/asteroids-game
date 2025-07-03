import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_loop(updatable_group, drawable_group)


def game_loop(updatable, drawable):
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        pygame.Surface.fill(screen, color="black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        


if __name__ == "__main__":
    main()
