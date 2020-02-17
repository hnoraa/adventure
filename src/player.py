# player.py
# main player sprite
import pygame
from settings import *

from common.f_directories import imagesDir
from common.spriteSheet import SpriteSheet

from sprite import Sprite, collide

vec = pygame.math.Vector2


# class Player(pygame.sprite.Sprite):
class Player(Sprite):
    def __init__(self, game, x, y):
        self.spriteSheet = SpriteSheet(PLAYER_SPRITE)

        # directional images
        # TODO: this needs to be updated, need 32 x 32 character sprite so we don't have to call transform
        self.images = [
            self.spriteSheet.image_at((0, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),     # up
            self.spriteSheet.image_at((32, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),    # down
            self.spriteSheet.image_at((64, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),    # left
            self.spriteSheet.image_at((96, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)     # right
        ]
        
        self.image = self.images[0]
        super().__init__(game, PLAYER_HIT_RECT, self.image, x, y)

    def getKeys(self):
        self.vel = vec(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = 'l'
            self.vel.x = -PLAYER_SPEED

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = 'r'
            self.vel.x = PLAYER_SPEED

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = 'u'
            self.vel.y = -PLAYER_SPEED

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = 'd'
            self.vel.y = PLAYER_SPEED

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= VEL_FACTOR

    def getImageFromDirection(self):
        if self.direction == 'l':
            self.image = self.images[2]
        elif self.direction == 'r':
            self.image = self.images[3]
        elif self.direction == 'u':
            self.image = self.images[0]
        else:
            self.image = self.images[1]

    def update(self):
        self.getKeys()

        # depending on which key was pressed, load the appropriate image (up, down, left, right)
        self.getImageFromDirection()

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.pos += self.vel * self.game.dt

        self.hitRect.centerx = self.pos.x
        collide(self, self.game.water, 'x')
        collide(self, self.game.stones, 'x')

        self.hitRect.centery = self.pos.y
        collide(self, self.game.water, 'y')
        collide(self, self.game.stones, 'y')

        self.rect.center = self.hitRect.center
