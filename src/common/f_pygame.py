# f_pygame.py
# pygame functions
import pygame
from . import f_directories

def mainGameEvents(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    return running

def loadImage(fileName, isAlpha=True):
    if isAlpha:
        image = pygame.image.load(f_directories.imagesDir(fileName)).convert_alpha()
    else:
        image = pygame.image.load(f_directories.imagesDir(fileName)).convert()
    return image

def loadScaledImage(fileName, scaleX, scaleY, isAlpha=True):
    image = loadImage(fileName, isAlpha)

    image = pygame.transform.scale(image, (scaleX, scaleY))
    return image

def collideHitRect(one, two):
    return one.hitRect.colliderect(two.rect)

def getHits(sprite, group):
    return pygame.sprite.spritecollide(sprite, group, False, collideHitRect)