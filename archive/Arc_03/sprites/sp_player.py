# sp_player.py
import pygame

from settings import *
from common.f_pygame import vec
from common.spriteSheet import SpriteSheet
from .sprite import Sprite


class Player(Sprite):
    def __init__(self, game, x, y, debug=False):
        self.debug = debug

        self.spriteSheet = SpriteSheet(PLAYER_SPRITE)
        self.images = [
            self.spriteSheet.image_at((0, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),  # up
            self.spriteSheet.image_at((32, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),  # down
            self.spriteSheet.image_at((64, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY),  # left
            self.spriteSheet.image_at((96, 0, PLAYER_SIZE, PLAYER_SIZE), COLOR_KEY)  # right
        ]

        self.image = self.images[0]
        super().__init__(game, PLAYER_HIT_RECT, self.image, x, y)

    def setPosition(self, x, y):
        super().setPosition(x, y)

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
        super().update()

        # get the keys pressed
        self.getKeys()

        # depending on which key was pressed, load the appropriate image (up, down, left, right)
        self.getImageFromDirection()

        # get the players rect from the image and set the center to the current player position
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # update the players position
        self.pos += self.vel * self.game.dt

        # set the hit rect to the player position
        self.hitRect.centerx = self.pos.x
        self.hitRect.centery = self.pos.y

        # set the player rect as a result of any collisions
        self.rect.center = self.hitRect.center

        # if debug limit to bounds of screen
        if self.debug:
            print(self.game.screen.get_rect())
            print(self.rect)
            self.rect.clamp(self.game.screen.get_rect())
