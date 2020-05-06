# settings.py
# game settings
import pygame


# colors and transparency key
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLOR_KEY = MAGENTA

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 60
CLOCK_TICK = 1000
TITLE = "Tile Adventure"

# subdirectories
IMG_DIR = '../images'
MAP_DIR = '../res/maps'

# player settings
PLAYER_SPEED = 300
PLAYER_SIZE = 32
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
VEL_FACTOR = 0.7071
PLAYER_SPRITE = 'catSpriteSheet1.png'
