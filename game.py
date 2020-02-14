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