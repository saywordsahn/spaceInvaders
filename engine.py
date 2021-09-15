import pygame
from sounds import Sounds
from player import Player
from heart import Heart
from aliens import Aliens
from alien_bullets import AlienBullets
from bullet import Bullet


class Engine:

    def __init__(self):
        pygame.init()
        self.sounds = Sounds(volume=.025)

        self.screen_width = 600
        self.screen_height = 800
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.game_over = False

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Space Invaders')

        self.bg = pygame.image.load('img/bg.png')

        # define fonts
        self.font30 = pygame.font.SysFont('Constantia', 30)
        self.font40 = pygame.font.SysFont('Constantia', 40)

        # player
        self.player = Player(self.screen_width, self.sounds)

        # heart
        self.heart_image = pygame.image.load('img/heart.png')
        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))

        # create groups
        self.hud_group = pygame.sprite.Group()

        for i in range(3):
            self.hud_group.add(Heart(self.heart_image, 480 + 40 * i, 10))

        self.player_group = pygame.sprite.Group(self.player)
        self.alien_group = Aliens()
        self.alien_group.generate()
        self.bullet_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.alien_bullet_group = AlienBullets(self.sounds.explosion2_fx, self.screen_height)

        self.keys = pygame.key.get_pressed()


    def input(self):
        time = pygame.time.get_ticks()
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_SPACE] and time - self.player.last_shot > self.player.gun_cooldown:
            self.sounds.laser_fx.play()
            bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
            self.bullet_group.add(bullet)
            self.player.last_shot = time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)

    def update(self):
        self.player.update(self.screen, self.keys, self.bullet_group, self.explosion_group)

        self.alien_group.update()

        for bullet in self.bullet_group:
            bullet.update(self.alien_group, self.explosion_group, self.sounds.explosion_fx)

        for explosion in self.explosion_group:
            explosion.update()

        self.alien_bullet_group.update(self.hud_group, self.alien_group, self.player_group, self.explosion_group)

        if len(self.explosion_group) == 0 and not self.player.alive:
            self.game_over = True

    def draw_text(screen, text, font, text_col, x, y):
        txt_img = font.render(text, True, text_col)
        screen.blit(txt_img, (x, y))

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        if self.game_over:
            self.draw_text(self.screen, 'Game Over!', self.font40, pygame.color.Color('white'), int(self.screen_width / 2 - 100),
                      int(self.screen_height / 2 + 50))
        else:
            self.player_group.draw(self.screen)
            self.alien_group.draw(self.screen)
            self.alien_bullet_group.draw(self.screen)
            self.bullet_group.draw(self.screen)
            self.explosion_group.draw(self.screen)
            self.hud_group.draw(self.screen)

        pygame.display.update()

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()
            self.clock.tick(self.FPS)