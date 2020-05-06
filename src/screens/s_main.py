import pygame
from src.common.settings import *
from .screenState import ScreenState

class MainScreen(ScreenState):
    def __index__(self, game):
        super().__init__(game, 'main')

    def events(self):
        super().events()

        if self.keys[pygame.K_RETURN]:
            # change state to main screen
            pass

    def update(self):
        super().update()

    def render(self):
        super().render()

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
