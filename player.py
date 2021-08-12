import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self, screen_width):
        self.player_image = pygame.image.load('img/spaceship.png')
        self.player_sprite = pygame.sprite.Sprite()
        self.player_sprite.image = self.player_image
        self.player_sprite.rect = self.player_image.get_rect()
        self.player_sprite.rect.centerx = 300
        self.player_sprite.rect.bottom = 760
        self.player_speed = 8
        self.screen_width = screen_width
        
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.player_sprite.rect.left > 0:
            self.player_sprite.rect.x -= self.player_speed

        if keys[pygame.K_RIGHT] and self.player_sprite.rect.right < self.screen_width:
            self.player_sprite.rect.x += self.player_speed
