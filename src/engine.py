"""
engine.py

Main game loop, basically the root of it all!
"""
import sys
import pygame


class Engine:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen_size = (100, 100)
        self.screen = pygame.display.set_mode(self.screen_size)

        pygame.display.set_caption('Adventure')

        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 0
        self.fps = 50
        self.clock_tick = 1000

    def run(self):
        while self.running:
            # update delta time var
            self.delta_time = self.clock.tick(50)

            self.process_events()

            self.process_updates()

            self.render()

        self.quit()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def process_updates(self):
        pass

    @staticmethod
    def render():
        pygame.display.flip()

    @staticmethod
    def quit():
        pygame.quit()

        sys.exit()
