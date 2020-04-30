import pygame
import sys

from common.f_pygame import mainGameEvents

from settings import *

# states
from state import StateMachine
from s_mainScreen import MainScreen

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()

        self.running = True
        self.getStates()        

    def getStates(self):
        self.states = StateMachine()

        self.states.addState('mainScreen', MainScreen(self))

        self.states.change('mainScreen')

    def loop(self):
        print(self.states.currentState.name)

        while self.running:
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            self.running = mainGameEvents(self.running)
            self.states.events()

            self.update()

            self.render()

        self.quit()

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def update(self):
        self.states.update()
        self.allSprites.update()

    def render(self):
        self.states.render()
        pygame.display.flip()
