# s_pauseScreen.py
import pygame

from settings import *
from state import State


# pause menu
class PauseMenu(State):
    def __init__(self, game):
        super().__init__(game, 'pauseScreen')
        self.lastState = None

    def events(self):
        super().events()

        if self.keys[pygame.K_e]:
            # return to last state
            self.game.states.change(self.game.states.lastState.name)

        if DEBUG and self.keys[pygame.K_q]:
            self.game.states.change('mainScreen')

    def update(self):
        super().update()

    def render(self):
        super().render()
        
        self.surface.fill(RED)
        self.game.screen.blit(self.surface, (0,0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
