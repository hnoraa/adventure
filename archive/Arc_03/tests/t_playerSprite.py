import pygame
import sys
from sprites import *
from settings import *
from common import *


class T_playerSprite():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('Player Sprite Test')

        self.clock = pygame.time.Clock()

        self.allSprites = pygame.sprite.Group()
        self.player = Player(self, 100, 100, True)

        self.running = True

    def loop(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / CLOCK_TICK

            self.running = mainGameEvents(self.running)

            # updates
            self.allSprites.update()
            self.player.update()

            # rendering
            self.screen.fill(WHITE)
            self.screen.blit(self.player.image, self.player.pos)
            pygame.display.flip()

        self.quit()

    def quit(self):
        pygame.quit()
        sys.exit()
