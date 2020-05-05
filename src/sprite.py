# sprite.py
import pygame

from settings import *
from common.f_pygame import getHits, vec


class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, hitRect, image, x, y):
        self.groups = game.allSprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = image
        self.hitRect = hitRect

        # set initial coordinates
        self.setPosition(x, y)

        self.direction = 'l'

    # set sprites positions
    def setPosition(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hitRect.center = self.rect.center

        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def update(self):
        pass