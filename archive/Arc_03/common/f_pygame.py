# f_pygame.py
# pygame functions
import pygame

from . import f_directories

vec = pygame.math.Vector2


def mainGameEvents(running):
    """
    Checks to see if the game is still running
    :param running: boolean flag for game running status
    :return: True if running, else False
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    return running


def loadImage(fileName, isAlpha=True):
    """
    Loads an image from pygame
    :param fileName: the filename (excluding directory path)
    :param isAlpha: if True convert_alpha() on image, else convert() on image
    :return: the image
    """
    if isAlpha:
        image = pygame.image.load(f_directories.imagesDir(fileName)).convert_alpha()
    else:
        image = pygame.image.load(f_directories.imagesDir(fileName)).convert()
    return image


def loadScaledImage(fileName, scaleX, scaleY, isAlpha=True):
    """
    Loads a scaled image from pygame
    :param fileName: the filename (excluding directory path)
    :param scaleX: the x scale factor
    :param scaleY: the y scale factor
    :param if True convert_alpha() on image, else convert() on image
    :return: the image
    """
    image = loadImage(fileName, isAlpha)

    image = pygame.transform.scale(image, (scaleX, scaleY))
    return image


def collideHitRect(one, two):
    """
    Detect collisions between to rects (objects)
    :param one: the object
    :param two: the object one is colliding with
    :return: the collision rect
    """
    return one.hitRect.colliderect(two.rect)


def getHits(sprite, group):
    """
    Detect sprite hits for a given sprite group
    :param sprite: the spite
    :param group: the sprite group the sprite is colliding with
    :return: sprite/group collisions
    """
    return pygame.sprite.spritecollide(sprite, group, False, collideHitRect)
