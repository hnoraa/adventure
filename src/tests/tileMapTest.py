# tileMapTest.py
# used to test functionality of .tmx files
import pygame
import os
import sys

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_pygame import mainGameEvents
import settings


class TileMapTest():
    def __init__(self):
        self.tilesize = settings.TILESIZE
        self.width = settings.WIDTH
        self.height = settings.HEIGHT

        self.running = True

        self.fps = settings.FPS
        
        pygame.init()
        self.clock = pygame.time.Clock()

        self.world = pygame.display.set_mode((self.width, self.height))
        self.map = pygame.Surface((self.width, self.height))
        self.tmxData = loadTmxFromFile('./maps/overworld_1.tmx')

    def load(self):
        self.map = renderTiledSurface(self.tmxData)
        self.mapRect = self.map.get_rect()

    def run(self):
        self.load()

        while self.running == True:
            self.running = mainGameEvents(self.running)

            self.draw()
            
            self.clock.tick(self.fps)

    def draw(self):
        self.world.blit(self.map, self.mapRect.topleft)
        pygame.display.flip()
    
    def drawTileMap(self):
        self.world.blit(self.map, self.mapRect.topleft)

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    t = TileMapTest()
    t.run()
