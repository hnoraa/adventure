"""
import pygame
import os
from globalVals import *

def setupFont(family, size):
    if flags.useCustomFont:
        return pygame.font.Font(os.path.join('assets', 'fonts', fonts.FCUST), size)
    else:
        return pygame.font.SysFont(family, size)

def renderText(msg, font, color):
    return font.render(msg, True, color)

def drawText(surface, textObj, x, y):
    surface.blit(textObj, (x, y))
"""
import pygame
from src.settings.st_game import *
from .f_directories import fontsDir


def setupFont(family, size, custom=False):
    """
    Set up a font
    :param family: font family
    :param size: size (pt)
    :param custom: if True custom font (*.ttf), else system font
    :return: pygame font object
    """
    if custom:
        return pygame.font.Font(fontsDir(family), size)
    else:
        return pygame.font.SysFont(family, size)


def renderText(msg, font, color):
    """
    Render the text
    :param msg: the message to render
    :param font: the font object
    :param color: the text color
    :return: rendered text object
    """
    return font.render(msg, True, color)


def drawText(surface, textObj, x, y):
    """
    Draw text object to a given surface
    :param surface: the surface to draw to
    :param textObj: the text object to draw
    :param x: x coordinate
    :param y: y coordinate
    """
    surface.blit(textObj, (x, y))
