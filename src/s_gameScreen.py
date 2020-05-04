# non local imports
import pygame

# states
from state import State

# game settings
from settings import *


# gameScreen
class GameScreen(State):
    def __init__(self, game):
        super().__init__(game, 'GameScreen')

    def events(self):
        super().events()

        if self.keys[pygame.K_p]:
            # call pause menu
            self.game.states.change('pause')

        if self.keys[pygame.K_q]:
            self.game.states.change('mainScreen')

    def update(self):
        super().update()

    def render(self):
        super().render()
        self.surface.fill(BROWN)
        self.game.screen.blit(self.surface, (0,0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()