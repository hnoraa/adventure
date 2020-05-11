# f_directories.py
# functions to get directory paths
from os import path
from src.settings import *


def rootDir():
    """
    Get the base directory
    :return: the base directory
    """
    return path.dirname(__file__)


def imagesDir(fileName):
    """
    Concatenates a filename with the images directory (defined in settings)
    :param fileName: image file name
    :return: the relative path to the image
    """
    return path.join(rootDir(), IMG_DIR, fileName)


def mapsDir(fileName):
    """
    Concatenates a filename with the maps directory (defined in settings)
    :param fileName: map file name
    :return: the relative path to the map
    """
    return path.join(rootDir(), MAP_DIR, fileName)


def fontsDir(fileName):
    """
    Concatenates a filename with the fonts directory (defined in settings)
    :param fileName: font file name
    :return: the relative path to the font
    """
    return path.join(rootDir(), FONT_DIR, fileName)
