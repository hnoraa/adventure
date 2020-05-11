# screenState.py
# management of the main game screen states
import pygame


class ScreenState:
    """
    Base class for screen states of the game
    """

    def __init__(self, game, name):
        self.name = name
        self.game = game
        self.surface = pygame.Surface(game.dimensions)
        self.surfaceRect = self.surface.get_rect()

    def events(self):
        self.keys = pygame.key.get_pressed()

    def update(self):
        pass

    def render(self):
        pass

    def onEnter(self):
        pass

    def onExit(self):
        pass


class ScreenStateMachine:
    """
    Screen state manager to handle switching and adding/removing states
    """

    def __init__(self):
        self.states = {}
        self.current = None
        self.last = None

    def events(self):
        if not self.current is None:
            self.current.events()

    def update(self):
        if not self.current is None:
            self.current.update()

    def render(self):
        if not self.current is None:
            self.current.render()

    def changeState(self, newStateName):
        if not self.current is None:
            self.current.onExit()

        # save the current state for backtracking
        self.last = self.current

        # get new state from state dict
        self.current = self.states[newStateName]

    def addState(self, newStateName, stateObj):
        self.states[newStateName] = stateObj
