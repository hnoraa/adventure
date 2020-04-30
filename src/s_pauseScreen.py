# non local imports
import pygame

# states
from state import State

# game settings
from settings import *


# pause menu
class PauseMenu(State):
    def __init__(self, game):
        super().__init__(game, 'pause')
        self.lastState = None

    def events(self):
        super().events()

        if self.keys[pygame.K_e]:
            # return to last state
            self.game.states.change(self.game.states.lastState.name)

        if self.keys[pygame.K_q]:
            self.game.states.change('mainScreen')

    def update(self):
        super().update()

    def render(self):
        super().render()
        self.surface.fill(RED)
        self.game.screen.blit(self.surface, (0,0))

    def onEnter(self):
        print(self.game.states.lastState.name)
        super().onEnter()

    def onExit(self):
        super().onExit()
        