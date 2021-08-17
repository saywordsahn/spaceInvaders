import pygame
import random
from alien_bullet import AlienBullet

class AlienBullets():

    def __init__(self, alien_explode_fx, screen_height):
        self.max_bullets = 5
        self.alien_bullet_cooldown = 1000
        self.last_shot = pygame.time.get_ticks()
        self.bullet_fx = alien_explode_fx
        self.screen_height = screen_height
        self.alien_bullet_image = pygame.image.load('img/alien_bullet.png').convert_alpha()

    def update(self, alien_bullet_group, alien_group, player_group, explosion_group):
        time = pygame.time.get_ticks()
        cooldown_passed = time - self.last_shot > 1000
        under_max_bullets_allowed = len(alien_bullet_group) < self.max_bullets

        if cooldown_passed and under_max_bullets_allowed and len(alien_group) > 0:
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = AlienBullet(self.alien_bullet_image,
                                       attacking_alien.rect.centerx,
                                       attacking_alien.rect.bottom,
                                       self.bullet_fx,
                                       self.screen_height)
            alien_bullet_group.add(alien_bullet)
            self.last_shot = time

        for bullet in alien_bullet_group:
            bullet.update(player_group, explosion_group)
