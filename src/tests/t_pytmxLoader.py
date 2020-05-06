# load tmx file and show it
import pytmx
import pygame
import sys

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
        x = min(0, x)   # left
        y = min(0, y)   # top
        x = max(-(self.width - 640), x)   # right
        y = max(-(self.height - 480), y) # bottom
        
        self.camera = pygame.Rect(x, y, self.width, self.height)


class TiledMap:
    def __init__(self, file):
        self.tmxdata = pytmx.load_pygame(file, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

    def render(self):
        surface = pygame.Surface((self.tmxdata.width * self.tmxdata.tilewidth, self.tmxdata.height * self.tmxdata.tileheight))
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
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

# load tmx
file = "../maps/old/overworld.tmx"
tmxFile = pytmx.load_pygame(file, pixelalpha=True)

# create surface
mapE = TiledMap(file)
mapImg = mapE.render()
mapE.rect = mapImg.get_rect()

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
    
    #update
    #camera.update()

    # render
    # screen.blit(mapSurf, camera.apply(mapE))
    screen.blit(mapImg, (0,0))
    pygame.display.flip()

# quit
pygame.quit()
sys.exit()