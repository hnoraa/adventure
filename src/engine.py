# engine.py
# top level game engine to hold states and base game loop logic
import sys

from src.screens import *


class Engine:
    """
    The main game engine
    """

    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.dimensions = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.dimensions)

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.states = screenState.ScreenStateMachine()
        self.states.addState('mainScreen', sc_main.MainScreen(self))
        self.states.addState('overworldScreen', sc_overworld.OverworldScreen(self))
        self.states.addState('pauseScreen', sc_pause.PauseScreen(self))
        self.states.changeState('mainScreen')

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
        self.states.events()

    def update(self):
        # do events of the current state
        self.states.update()

    def render(self):
        # do events of current state
        self.states.render()

        # flip the display
        pygame.display.flip()

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()
