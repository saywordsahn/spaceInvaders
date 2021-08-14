import pygame

class AlienBullet(pygame.sprite.Sprite):

    def __init__(self, image, x, y, explode_fx):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.explode_fx = explode_fx

    def update(self, screen_height, player_group):
        self.rect.y += 2
        if self.rect.top > screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask):
            self.kill()
            self.explode_fx.play()