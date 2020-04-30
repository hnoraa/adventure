import pygame

from state import State
from settings import *

class MainScreen(State):
    def __init__(self, game):
        super().__init__(game, 'mainScreen')
        self.gameSave = None

    def events(self):
        super().events()

        if self.keys[pygame.K_RETURN]:
            self.onExit()

    def update(self):
        super().update()

    def render(self):
        super().render()
        self.surface.fill(MAGENTA)
        self.game.screen.blit(self.surface, (0,0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
        self.game.gameSave = self.gameSave