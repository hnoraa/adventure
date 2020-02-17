# player.py
# main player sprite
import pygame
from settings import *

from common.f_directories import imagesDir
from common.spriteSheet import SpriteSheet

from maps import collideHitRect

vec = pygame.math.Vector2

def collide(sprite, group, direction):
    if direction == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collideHitRect)
        if hits:
            if hits[0].rect.centerx > sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hitRect.width / 2
            if hits[0].rect.centerx < sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hitRect.width / 2

            sprite.vel.x = 0
            sprite.hitRect.centerx = sprite.pos.x
    if direction == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collideHitRect)
        if hits:
            if hits[0].rect.centery > sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hitRect.height / 2
            if hits[0].rect.centery < sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hitRect.height / 2
        
        sprite.vel.y = 0
        sprite.hitRect.centery = sprite.pos.y


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.spriteSheet = SpriteSheet(PLAYER_SPRITE)

        # directional images
        self.images = [
            self.spriteSheet.image_at((30, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),
            self.spriteSheet.image_at((45, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),
            self.spriteSheet.image_at((0, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),
            self.spriteSheet.image_at((15, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)
        ]
        self.images[0] = pygame.transform.scale(self.images[0], (32, 32))
        self.images[1] = pygame.transform.scale(self.images[1], (32, 32))
        self.images[2] = pygame.transform.scale(self.images[2], (32, 32))
        self.images[3] = pygame.transform.scale(self.images[3], (32, 32))

        self.image = self.images[0]
        self.direction = 'l'

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hitRect = PLAYER_HIT_RECT
        self.hitRect.center = self.rect.center

        self.vel = vec(0, 0)
        self.pos = vec(x, y)

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
            self.vel *= 0.7071

    def getImageFromDirection(self):
        if self.direction == 'l':
            self.image = self.images[0]
        elif self.direction == 'r':
            self.image = self.images[1]
        elif self.direction == 'u':
            self.image = self.images[2]
        else:
            self.image = self.images[3]

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
