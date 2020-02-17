import pygame

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_directories import mapsDir

from settings import *


class TiledMap:
    def __init__(self):
        self.tmxdata = loadTmxFromFile(mapsDir(MAP_FILE))
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

    def render(self):
        return renderTiledSurface(self.tmxdata)
