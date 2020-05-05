# non local imports
import pygame
import sys

from settings import *
from common.f_pygame import mainGameEvents
from state import StateMachine
from s_mainScreen import MainScreen
from s_gameScreen import GameScreen
from s_pauseScreen import PauseMenu


# the main class of the game, it drives everything
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
        # add states to the game
        self.states = StateMachine()

        self.states.addState('mainScreen', MainScreen(self))
        self.states.addState('gameScreen', GameScreen(self))
        self.states.addState('pauseScreen', PauseMenu(self))

        self.states.change('mainScreen')

    def loop(self):
        print(self.states.currentState.name)

        while self.running:
            # update the delta time variable
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            # events
            self.running = mainGameEvents(self.running)
            self.states.events()

            # updates
            self.update()

            # rendering
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
