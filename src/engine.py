# engine.py
# top level game engine to hold states and base game loop logic
import pygame
import sys

from settings import *
from common.f_pygame import mainGameEvents

class Engine():
    def __init__(self):
        self.dimensions = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # update the delta time variable
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            # events
            self.events()

            # updates
            self.update()

            # rendering
            self.render()
        
        # terminate
        self.quit()

    def events(self):
        # process state events first
        self.running = mainGameEvents(self.running)

    def update(self):
        # do events of the current state
        pass

    def render(self):
        # do events of current state

        # flip the display
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

