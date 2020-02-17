import pygame

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_directories import mapsDir

from settings import *


class TiledMap:
    def __init__(self):
        self.tmxdata = loadTmxFromFile(mapsDir(MAP_FILE))

    def render(self):
        return renderTiledSurface(self.tmxdata)
