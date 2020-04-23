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
def enter(sprite, group):
    hits = getHits(sprite, group)
    if hits:
        # get the entrance name (corresponds to level/tunnel)
        if '_t' in hits[0].name:
            entranceName = hits[0].name.split('_')[1] + '_' + hits[0].name.split('_')[2]
        else:    
            entranceName = hits[0].name.split('_')[1]

        sprite.game.loadSubLevel(entranceName)


# used to exit to the overworld
def exitToOverworld(sprite, group):
    hits = getHits(sprite, group)
    if hits:
        sprite.game.loadOverworld(sprite.game.currentLocation)


# generic sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, game, hitRect, image, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = image
        self.hitRect = hitRect

        # set the initial coordinates
        self.setNewBounds(x, y)

        self.direction = 'l'

    # set the players bounds upon entrance/exit into another map
    def setNewBounds(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.hitRect.center = self.rect.center
        
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def update(self):
        pass
