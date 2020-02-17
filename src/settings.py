# settings.py
# game settings
import pygame as pg
vec = pg.math.Vector2

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
WIDTH = 600   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
CLOCK_TICK = 1000
TITLE = "Tile Adventure"

# subdirectories
IMG_DIR = '../images'
MAP_DIR = '../maps'

# files
MAP_FILE = 'overworld_2.tmx'
PLAYER_SPRITE = 'cat_sprite_1.png'

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_SPEED = 300
PLAYER_SIZE = 16
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
