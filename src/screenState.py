# screenState.py
# management of the main game screen states
import pygame


'''
Base class for screen states of the game
'''
class ScreenState():
    def __init__(self, game, name):
        self.name = name
        self.game = game


'''
Screen state manager to handle switching and adding/removing states
'''
class ScreenStateMachine():
    def __init__(self):
        pass

    def quit(self):
        pass