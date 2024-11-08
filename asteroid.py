from constants import *
from circleshape import *
from asteroidfield import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius >= ASTEROID_MIN_RADIUS:
            self.kill()
        
        random_angle = random.uniform(20, 50)
        
        
        old_radius = self.radius
        self.radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position, self.position, self.radius)
        asteroid2 = Asteroid(self.position, self.position, self.radius)
        asteroid1.velocity = (pygame.math.Vector2.rotate(self.velocity, random_angle)) * 1.2
        asteroid2.velocity = (pygame.math.Vector2.rotate(self.velocity, -random_angle)) * 1.2
