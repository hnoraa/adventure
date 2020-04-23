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
        self.currentLocation = 'o'
        self.allSprites = pygame.sprite.Group()
        
        self.player = Player(self, 0, 0)

    def run(self):
        self.load(self.currentLocation)

        while self.running:
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            self.running = mainGameEvents(self.running)

            self.update()

            self.draw()

        self.quit()

    def load(self, entranceName):
        # loads 
        self.currentLocation = entranceName

        self.map = TiledMap(self.currentLocation)
        self.mapImg = self.map.render()
        self.map.rect = self.mapImg.get_rect()
        
        # sprite groups
        self.water = pygame.sprite.Group()
        self.stones = pygame.sprite.Group()
        self.houses = pygame.sprite.Group()
        self.levelEntrances = pygame.sprite.Group()
        self.tunnelEntrances = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()

        for tileObj in self.map.tmxdata.objects:
            objCenter = vec(tileObj.x + tileObj.width / 2,
                             tileObj.y + tileObj.height / 2)

            if tileObj.name == 'player_'+self.currentLocation:
                self.player.setNewBounds(objCenter.x, objCenter.y)

            # overworld only
            if self.currentLocation == 'o':
                if '_l' in tileObj.name:
                    Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.levelEntrances, tileObj.name)

                if '_t' in tileObj.name:
                    Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.tunnelEntrances, tileObj.name)

            # obstacles
            if tileObj.name == 'water':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.water, tileObj.name)

            if tileObj.name == 'stone':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.stones, tileObj.name)

            if tileObj.name == 'house':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.houses, tileObj.name)

            if tileObj.name == 'wall':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.walls, tileObj.name)

            if tileObj.name == 'door':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.doors, tileObj.name)

            if tileObj.name == 'exit':
                Obstacle(self, tileObj.x, tileObj.y, tileObj.width, tileObj.height, self.exits, tileObj.name)

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
