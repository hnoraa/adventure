# player.py
# main player sprite
import pygame
from settings import *

from common.f_directories import imagesDir
from common.spriteSheet import SpriteSheet

vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.spriteSheet = SpriteSheet(PLAYER_SPRITE)

        self.imageLeft = self.spriteSheet.image_at((30, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)
        self.imageLeft = pygame.transform.scale(self.imageLeft, (32, 32))
        self.imageRight = self.spriteSheet.image_at((45, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)
        self.imageRight = pygame.transform.scale(self.imageRight, (32, 32))
        self.imageUp = self.spriteSheet.image_at((0, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)
        self.imageUp = pygame.transform.scale(self.imageUp, (32, 32))
        self.imageDown = self.spriteSheet.image_at((15, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)
        self.imageDown = pygame.transform.scale(self.imageDown, (32, 32))

        self.image = self.imageLeft

        self.rect = self.image.get_rect()
        self.hitRect = PLAYER_HIT_RECT
        self.hitRect.center = self.rect.center
        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE

    def get_keys(self):
        self.vel = vec(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.image = self.imageLeft
            self.vel.x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.image = self.imageRight
            self.vel.x = PLAYER_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.image = self.imageUp
            self.vel.y = -PLAYER_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.image = self.imageDown
            self.vel.y = PLAYER_SPEED
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def update(self):
        self.get_keys()

        # depending on which key was pressed, load the appropriate image (up, down, left, right)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hitRect.centerx = self.pos.x
        self.hitRect.centery = self.pos.y
        self.rect.center = self.hitRect.center
        self.rect.clamp_ip(self.game.currentWorldSurfaceRect)
