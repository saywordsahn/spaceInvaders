import pygame
import random

from player import Player
from alien import Alien
from bullet import Bullet
from alien_bullets import AlienBullets
from sounds import Sounds
from aliens import Aliens
from heart import Heart

def draw_text(text, font, text_col, x, y):
    txt_img = font.render(text, True, text_col)
    screen.blit(txt_img, (x, y))

pygame.init()
sounds = Sounds(volume=.025)

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60
game_over = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load('img/bg.png')

#define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

# player
player = Player(screen_width, sounds)

# heart
heart_image = pygame.image.load('img/heart.png')
heart_image = pygame.transform.scale(heart_image, (30, 30))

# create groups
hud_group = pygame.sprite.Group()

for i in range(3):
    hud_group.add(Heart(heart_image, 480 + 40 * i, 10))

player_group = pygame.sprite.Group(player)
alien_group = Aliens()
alien_group.generate()
bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
alien_bullet_group = AlienBullets(sounds.explosion2_fx, screen_height)

while True:
    time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and time - player.last_shot > player.gun_cooldown:
        sounds.laser_fx.play()
        bullet = Bullet(player.rect.centerx, player.rect.top)
        bullet_group.add(bullet)
        player.last_shot = time


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)


    player.update(screen, keys, bullet_group, explosion_group)

    alien_group.update()

    for bullet in bullet_group:
        bullet.update(alien_group, explosion_group, sounds.explosion_fx)

    for explosion in explosion_group:
        explosion.update()

    alien_bullet_group.update(hud_group, alien_group, player_group, explosion_group)


    if len(explosion_group) == 0 and not player.alive:
        game_over = True

    # update screen
    screen.blit(bg, (0, 0))

    if game_over:
        draw_text('Game Over!', font40, pygame.color.Color('white'), int(screen_width / 2 - 100), int(screen_height / 2 + 50))
    else:
        player_group.draw(screen)
        alien_group.draw(screen)
        alien_bullet_group.draw(screen)
        bullet_group.draw(screen)
        explosion_group.draw(screen)
        hud_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)