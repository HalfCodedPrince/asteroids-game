from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "white", self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        first_split = Asteroid(self.position.x, self.position.y, new_radius)
        second_split = Asteroid(self.position.x, self.position.y, new_radius)
        first_split.velocity = self.velocity.rotate(new_random_angle) * 1.2
        second_split.velocity = self.velocity.rotate(-new_random_angle) * 1.2
