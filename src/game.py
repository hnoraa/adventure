import pygame
import sys

from common.f_pygame import mainGameEvents

from settings import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.allSprites = pygame.sprite.Group()

        self.states = None
        self.currentState = None
        self.running = False


    def loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            self.running = mainGameEvents(self.running)

            self.update()

            self.draw()

        self.quit()

    def quit(self):
        self.running = False
        pygame.quit()
        sys.exit()

    def update(self):
        self.allSprites.update()

    def draw(self):
        pygame.display.flip()
