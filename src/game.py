# game.py
# the main game components
import pygame
import os
import sys

from common.f_pytmx import renderTiledSurface, loadTmxFromFile
from common.f_pygame import mainGameEvents
from common.f_directories import mapsDir

from settings import *
from camera import *
from player import *


class Game():
    def __init__(self):
        pygame.init()

        self.dimensions = (WIDTH, HEIGHT)

        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

    def run(self):
        self.load()
        while self.running:
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            self.running = mainGameEvents(self.running)

            self.update()

            self.draw()

        self.quit()

    def load(self):
        self.tmxData = loadTmxFromFile(mapsDir(MAP_FILE))
        self.overworldDim = (self.tmxData.width * self.tmxData.tilewidth, self.tmxData.height * self.tmxData.tileheight)
        self.map = renderTiledSurface(self.tmxData)
        self.mapRect = self.map.get_rect()

        self.camera = Camera(self.overworldDim[0], self.overworldDim[1])

        self.currentWorldSurface = self.map
        self.currentWorldSurfaceRect = self.currentWorldSurface.get_rect()

        self.allSprites = pygame.sprite.Group()
        self.player = Player(self, 10, 10)


        """ 
        Add obstacles for water and rock
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'zombie':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)
            if tile_object.name in ['health', 'shotgun']:
                Item(self, obj_center, tile_object.name) 
        """

    def update(self):
        self.allSprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.blit(self.currentWorldSurface, self.camera.applyRect(self.currentWorldSurfaceRect))

        for sprite in self.allSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pygame.display.flip()
    
    def quit(self):
        pygame.quit()
        sys.exit()
