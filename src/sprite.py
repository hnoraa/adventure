import pygame

from common.f_pygame import getHits

vec = pygame.math.Vector2

def collide(sprite, group, direction):
    if direction == 'x':
        hits = getHits(sprite, group)
        if hits:
            if hits[0].rect.centerx > sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hitRect.width / 2
            if hits[0].rect.centerx < sprite.hitRect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hitRect.width / 2

            sprite.vel.x = 0
            sprite.hitRect.centerx = sprite.pos.x
    if direction == 'y':
        hits = getHits(sprite, group)
        if hits:
            if hits[0].rect.centery > sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hitRect.height / 2
            if hits[0].rect.centery < sprite.hitRect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hitRect.height / 2
        
        sprite.vel.y = 0
        sprite.hitRect.centery = sprite.pos.y


class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, hitRect, image, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hitRect = hitRect
        self.hitRect.center = self.rect.center
        
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

        self.direction = 'l'

    def update(self):
        pass