# state.py
import pygame

from settings import *


# base class for states
class State():
    def __init__(self, game, name):
        self.map = None
        self.game = game
        self.surface = pygame.Surface(SCREEN_DIM)
        self.surfaceRect = self.surface.get_rect()
        self.name = name
        
    def loadMap(self):
        self.map = None

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


# for controlling the states in the game
class StateMachine():
    def __init__(self):
        self.states = {}
        self.currentState = None
        self.lastState = None
    
    def events(self):
        if not self.currentState is None:
            # events
            self.currentState.events()

    def update(self):
        if not self.currentState is None:
            # update the state
            self.currentState.update()

    def render(self):
        if not self.currentState is None:
            # render the state
            self.currentState.render()

    def change(self, newState):
        if not self.currentState is None:
            # exit current state
            self.currentState.onExit()

        # save the current state as the last state for back tracking (i.e. returning from pause menu or back to the overworld from a sub state)
        self.lastState = self.currentState

        # get new state from the array of states
        self.currentState = self.states[newState]

        # enter new state
        self.currentState.onEnter()

    def addState(self, newState, state):
        # add a state to the states dict
        self.states[newState] = state
