# camera.py
import pygame

from settings import *


class Camera():
    def __init__(self, w, h):
        self.camera = pygame.Rect(0, 0, w, h)
        self.w = w
        self.h = h

    def apply(self, ent):
        return ent.rect.move(self.camera.topleft)

    def applyRect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(SCREEN_DIM[0] / 2)
        y = -target.rect.centery + int(SCREEN_DIM[1] / 2)

        # limit scrolling to map size
        x = min(0, x)                           # left
        y = min(0, y)                           # top
        x = max(-(self.w - SCREEN_DIM[0]), x)   # right
        x = max(-(self.h - SCREEN_DIM[1]), y)   # bottom

        self.camera = pygame.Rect(x, y, self.w, self.h)
