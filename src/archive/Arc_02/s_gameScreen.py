# s_gameScreen.py
import pygame

from settings import *
from common.f_pygame import mainGameEvents
from common.f_pytmx import getObjCenter
from state import State
from maps import TiledMap
from camera import Camera


# gameScreen
class GameScreen(State):
    def __init__(self, game):
        super().__init__(game, 'gameScreen')

        self.maps = [
            "om_01",
            "om_02",
            "om_03"
        ]

        self.currentMap = self.maps[0]

    def events(self):
        super().events()

        if self.keys[pygame.K_p]:
            # call pause menu
            self.game.states.change('pauseScreen')

        if DEBUG and self.keys[pygame.K_q]:
            self.game.states.change('mainScreen')

    def update(self):
        super().update()
        self.game.camera.update(self.game.player)

    def render(self):
        self.surface.blit(self.mapImg, self.game.camera.apply(self.map))
        
        for spr in self.game.allSprites:
            self.surface.blit(spr.image, self.game.camera.apply(spr))

        super().render()

    def onEnter(self):
        super().onEnter()
        self.loadMap()

    def onExit(self):
        super().onExit()

    def loadMap(self):
        self.map = TiledMap(self.currentMap)
        self.mapImg = self.map.render()
        self.map.rect = self.mapImg.get_rect()

        self.game.camera = Camera(self.map.width, self.map.height)
