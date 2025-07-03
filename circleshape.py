import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    # I keep forgetting the logic, so it's verbose
    # basically, if the distance between circle objects is less (or equal) their radius, they are touching. If I forget again, just picture or draw it.
    def is_colliding(self, other_circle):
        collision = False
        if self.position.distance_to(other_circle.position) <= (self.radius + other_circle.radius):
            collision = True
        return collision
