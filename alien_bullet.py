import pygame
from explosion import Explosion


class AlienBullet(pygame.sprite.Sprite):

    def __init__(self, image, x, y, explode_fx, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.explode_fx = explode_fx
        self.screen_height = screen_height
        self.bullet_speed = 2

    def update(self, hud_group: pygame.sprite.Group, player_group, explosion_group):
        self.rect.y += self.bullet_speed
        if self.rect.top > self.screen_height:
            self.kill()
        if pygame.sprite.spritecollide(self, player_group, False, pygame.sprite.collide_mask):
            self.kill()
            self.explode_fx.play()
            # bad practice... there's only 1 player

            for player in player_group:
                player.health -= 1
                hud_group.sprites()[len(hud_group.sprites()) - 1].kill()
                explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
                explosion_group.add(explosion)