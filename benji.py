import pygame

from player import Player

pygame.init()

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load('img/bg.png')

# player
player = Player(screen_width)

player_group = pygame.sprite.Group(player.player_sprite)


while True:

    keys = pygame.key.get_pressed()

    player.update(keys)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.blit(bg, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)