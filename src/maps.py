import pygame

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_directories import mapsDir

from settings import *


class TiledMap:
    def __init__(self, location):
        self.location = location

        if self.location == 'o':
            self.tmxdata = loadTmxFromFile(mapsDir(MAP_FILE))
            self.width = self.tmxdata.width * self.tmxdata.tilewidth
            self.height = self.tmxdata.height * self.tmxdata.tileheight
            self.mapType = 'overworld'
        else:
            mapName = location[:2] + '.tmx'

            if location[0] == 'l' or location[0] == 't':
                # level
                self.tmxdata = loadTmxFromFile(mapsDir(mapName))
                self.width = self.tmxdata.width * self.tmxdata.tilewidth
                self.height = self.tmxdata.height * self.tmxdata.tileheight
                
                if location[0] == 'l':
                    self.mapType = 'level'
                else:
                    self.mapType = 'tunnel'
            else:
                # other (house, shop, etc...)
                pass

    def render(self):
        return renderTiledSurface(self.tmxdata)
