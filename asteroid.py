from constants import *
from circleshape import *
from asteroidfield import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), 2)
    
    def update(self, dt):
        self.x += (3 * dt)
        self.y += (3 * dt)
    
