import pygame
from explosion import Explosion

class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.bottom = 760
        self.player_speed = 8
        self.screen_width = screen_width
        self.last_shot = pygame.time.get_ticks()
        self.gun_cooldown = 300
        self.health = 3
        self.alive = True

    def update(self, keys, explosion_group):

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.player_speed

        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.player_speed

        if self.health <= 0 and self.alive == True:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()
            self.alive = False
