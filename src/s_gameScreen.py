# s_gameScreen.py
import pygame

from settings import *
from common.f_pygame import mainGameEvents
from common.f_pytmx import getObjCenter
from state import State
from maps import TiledMap


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

    def render(self):
        self.game.screen.blit(self.mapImg, (0,0))
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

