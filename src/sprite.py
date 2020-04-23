# sprite.py
# parent sprite class to inherit from
import pygame

from common.f_pygame import getHits

vec = pygame.math.Vector2


# object collision
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


# used to enter a level or tunnel
def enter(sprite, group, direction):
    if direction == 'x':
        hits = getHits(sprite, group)
        if hits:
            # get the entrance name (corresponds to level/tunnel)
            entranceName = hits[0].name.split('_')[1]
            print(entranceName)

            if 'l' in entranceName:
                print('level')
            else:
                print('tunnel')

    if direction == 'y':
        hits = getHits(sprite, group)
        if hits:
            # get the entrance name (corresponds to level/tunnel)
            entranceName = hits[0].name.split('_')[1]
            print(entranceName)

            if 'l' in entranceName:
                print('level')
            else:
                print('tunnel')


# generic sprite class
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
        self.aquatic = True

    def update(self):
        pass
