import pygame
from pygame import mixer

from player import Player
from alien import Alien
from bullet import Bullet
from alien_bullets import AlienBullets

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60

rows = 5
cols = 5


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load('img/bg.png')

# load sounds
laser_fx = pygame.mixer.Sound('img/laser.wav')
laser_fx.set_volume(0.25)

explosion_fx = pygame.mixer.Sound("img/explosion.wav")
explosion_fx.set_volume(0.25)

explosion2_fx = pygame.mixer.Sound("img/explosion2.wav")
explosion2_fx.set_volume(0.25)

# player
player = Player(screen_width)

# create groups
player_group = pygame.sprite.Group(player)
alien_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()

# alien
alien = Alien(200, 200)
alien_bullets = AlienBullets(explosion2_fx, screen_height)

# add aliens
for row in range(rows):
    for col in range(cols):
        alien = Alien(100 + col * 100, 100 + row * 70)
        alien_group.add(alien)





while True:
    time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and time - player.last_shot > player.gun_cooldown:
        laser_fx.play()
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


    player.update(keys)

    for alien in alien_group:
        alien.update()

    for bullet in bullet_group:
        bullet.update(alien_group, explosion_group, explosion_fx)

    for explosion in explosion_group:
        explosion.update()

    alien_bullets.update(alien_bullet_group, alien_group, player_group)

    # update screen
    screen.blit(bg, (0, 0))
    player_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    bullet_group.draw(screen)
    explosion_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)