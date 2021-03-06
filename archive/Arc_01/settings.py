# st_game.py
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
MAP_DIR = '../maps'

# files
MAP_FILE = 'overworld.tmx'
LEVEL1_FILE = 'l1.tmx'
LEVEL2_FILE = 'l2.tmx'
LEVEL3_FILE = 'l3.tmx'
LEVEL4_FILE = 'l4.tmx'
TUNNEL1_FILE = 't1.tmx'
TUNNEL2_FILE = 't2.tmx'
PLAYER_SPRITE = 'catSpriteSheet1.png'

# player settings
PLAYER_SPEED = 300
PLAYER_SIZE = 32
PLAYER_HIT_RECT = pygame.Rect(0, 0, 35, 35)
VEL_FACTOR = 0.7071
