import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen_width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.bottom = 760
        self.player_speed = 8
        self.screen_width = screen_width
        
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.player_speed

        if keys[pygame.K_RIGHT] and self.rect.right < self.screen_width:
            self.rect.x += self.player_speed
