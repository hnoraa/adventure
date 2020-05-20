# load tmx file and show it
import sys

import pygame
import pytmx

vec = pygame.math.Vector2


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def applyRect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(640 / 2)
        y = -target.rect.centery + int(480 / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - 640), x)  # right
        y = max(-(self.height - 480), y)  # bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        self.groups = groups

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.hitRect = pygame.Rect(0, 0, 35, 35)
        self.rect = pygame.Rect(0, 0, 35, 35)

        # set initial coordinates
        self.setPosition(x, y)

        self.direction = 'l'

    def setPosition(self, x, y):

        self.rect.center = (x, y)
        self.hitRect.center = self.rect.center

        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def getKeys(self):
        self.vel = vec(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction = 'l'
            self.vel.x = -120

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction = 'r'
            self.vel.x = 120

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction = 'u'
            self.vel.y = -120

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction = 'd'
            self.vel.y = 120

        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071

    def update(self):
        self.getKeys()

        self.rect.center = self.pos

        # update the players position
        self.pos += self.vel * 0.03

        # set the hit rect to the player position
        self.hitRect.centerx = self.pos.x
        self.hitRect.centery = self.pos.y

        # set the player rect as a result of any collisions
        self.rect.center = self.hitRect.center


class TiledMap:
    def __init__(self, file):
        self.tmxdata = pytmx.load_pygame(file, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

    def render(self):
        surface = pygame.Surface(
            (self.tmxdata.width * self.tmxdata.tilewidth, self.tmxdata.height * self.tmxdata.tileheight))
        ti = self.tmxdata.get_tile_image_by_gid

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

        return surface


# init pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

# load tmx
file = "../res/maps/overworld.tmx"
tmxFile = pytmx.load_pygame(file, pixelalpha=True)

# create surface
mapE = TiledMap(file)
mapImg = mapE.render()
mapE.rect = mapImg.get_rect()

# create a player
allSprites = pygame.sprite.Group()
player = Player(10, 10, allSprites)

camera = Camera(mapE.width, mapE.height)

# main loop
running = True
while running:
    # events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
    player.getKeys()

    # update
    allSprites.update()
    camera.update(player)

    # render
    screen.blit(mapImg, camera.apply(mapE))
    # screen.blit(mapImg, (0, 0))
    pygame.display.flip()

# quit
pygame.quit()
sys.exit()
