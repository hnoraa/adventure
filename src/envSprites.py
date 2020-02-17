# envSprites.py
# used for items and world objects (ie. water, rock)
# these are sprites that player collides with that may not have a sprite image
import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h, spriteGroup):
        self.groups = spriteGroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x, y, w, h)
        self.hitRect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y