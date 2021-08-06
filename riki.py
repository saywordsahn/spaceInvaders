import pygame

pygame.init()

screen_width = 600
screen_height = 800
clock = pygame.time.Clock()
FPS = 60


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')

bg = pygame.image.load('img/bg.png')

# player
player_image = pygame.image.load('img/spaceship.png')
player_sprite = pygame.sprite.Sprite()
player_sprite.image = player_image
player_sprite.rect = player_image.get_rect()
player_sprite.rect.centerx = 300
player_sprite.rect.bottom = 760
player_speed = 8


player_group = pygame.sprite.Group(player_sprite)


while True:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_sprite.rect.left > 0:
        player_sprite.rect.x -= player_speed

    if keys[pygame.K_RIGHT] and player_sprite.rect.right < screen_width:
        player_sprite.rect.x += player_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.blit(bg, (0, 0))
    player_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)