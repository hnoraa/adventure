# f_directories.py
# functions to get directory paths
from os import path
from settings import *

def rootDir():
    return path.dirname(__file__)

def imagesDir(fileName):
    return path.join(rootDir(), IMG_DIR, fileName)

def mapsDir(fileName):
    return path.join(rootDir(), MAP_DIR, fileName)
    