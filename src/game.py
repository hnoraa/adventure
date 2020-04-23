# game.py
# the main game components
import pygame
import os
import sys

from common.f_pygame import mainGameEvents

from settings import *
from camera import Camera
from player import Player
from envSprites import Obstacle
from maps import TiledMap


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
        self.map = TiledMap()
        self.mapImg = self.map.render()
        self.map.rect = self.mapImg.get_rect()

        self.allSprites = pygame.sprite.Group()
        self.water = pygame.sprite.Group()
        self.stones = pygame.sprite.Group()
        self.houses = pygame.sprite.Group()
        self.levelEntrances = pygame.sprite.Group()
        self.tunnelEntrances = pygame.sprite.Group()

        for tileObj in self.map.tmxdata.objects:
            objCenter = vec(tileObj.x + tileObj.width / 2,
                             tileObj.y + tileObj.height / 2)

            if tileObj.name == 'player':
                self.player = Player(self, objCenter.x, objCenter.y)

            if tileObj.name == 'water':
                Obstacle(self, tileObj.x, tileObj.y,
                         tileObj.width, tileObj.height, self.water, tileObj.name)
                         
            if tileObj.name == 'stone':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.stones, tileObj.name)

            if tileObj.name == 'house':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.houses, tileObj.name)

            if '_l' in tileObj.name:
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.levelEntrances, tileObj.name)

            if '_t' in tileObj.name:
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.tunnelEntrances, tileObj.name)

        self.camera = Camera(self.map.width, self.map.height)

    def update(self):
        self.allSprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.blit(self.mapImg, self.camera.apply(self.map))

        for sprite in self.allSprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pygame.display.flip()
    
    def quit(self):
        pygame.quit()
        sys.exit()
