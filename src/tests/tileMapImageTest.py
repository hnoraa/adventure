import pygame
import os
import sys


class TileMapImageTest():
    def __init__(self):
        self.height = 192
        self.width = 320

        self.running = True

        self.fps = 60

        self.clock = pygame.time.Clock()
        pygame.init()

        self.world = pygame.display.set_mode([self.width, self.height])
        self.background = pygame.image.load(os.path.join('images', 'tile_set_test_1.png'))
        self.backgroundRect = self.background.get_rect()

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        self.running = False

            self.world.blit(self.background, self.backgroundRect)

            pygame.display.flip()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    t = TileMapImageTest()
    t.run()
    