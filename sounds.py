import pygame
from pygame import mixer

class Sounds:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()

        self.laser_fx = pygame.mixer.Sound('img/laser.wav')
        self.laser_fx.set_volume(0.25)

        self.explosion_fx = pygame.mixer.Sound("img/explosion.wav")
        self.explosion_fx.set_volume(0.25)

        self.explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
        self.explosion2_fx.set_volume(0.25)