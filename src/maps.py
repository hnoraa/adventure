import pygame

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_directories import mapsDir

from settings import *


class TiledMap:
    def __init__(self):
        tm = loadTmxFromFile(mapsDir(MAP_FILE))
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self):
        return renderTiledSurface(self.tmxdata)
