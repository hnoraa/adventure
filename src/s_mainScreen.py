# non local imports
import pygame

# states
from state import State

# game settings
from settings import *


# main start screen
class MainScreen(State):
    def __init__(self, game):
        super().__init__(game, 'mainScreen')
        self.gameSave = None

    def events(self):
        super().events()

        # load the main world
        if self.keys[pygame.K_RETURN]:
            self.game.states.change('gameScreen')

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
        