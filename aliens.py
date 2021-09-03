import pygame
import random
from alien import Alien

class Aliens(pygame.sprite.Group):

    def __init__(self):
        pygame.sprite.Group.__init__(self)
        self.rows = 5
        self.cols = 5

    def generate(self):
        alien_images = []
        for i in range(1, 5):
            loc = 'img/alien' + str(i) + '.png'
            img = pygame.image.load(loc)
            alien_images.append(img)

        for row in range(self.rows):
            for col in range(self.cols):
                alien = Alien(random.choice(alien_images), 100 + col * 100, 100 + row * 70)
                self.add(alien)

    def update(self):
        for alien in self:
            alien.update()