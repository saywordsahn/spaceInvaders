import pygame

class AlienBullet(pygame.sprite.Sprite):

    def __init__(self, image, x, y, explode_fx, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.explode_fx = explode_fx
        self.screen_height = screen_height

    def update(self, player_group):
        self.rect.y += 2
        if self.rect.top > self.screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask):
            self.kill()
            self.explode_fx.play()