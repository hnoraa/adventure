# maps.py
import pygame

from settings import *
from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_directories import mapsDir


class TiledMap:
    def __init__(self, mapName):
        self.tmxdata = loadTmxFromFile(mapsDir(mapName + '.tmx'))
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

    def render(self):
        return renderTiledSurface(self.tmxdata)
