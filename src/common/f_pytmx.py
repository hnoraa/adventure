import pytmx
import pygame

def loadTmxFromFile(fileName):
    return pytmx.load_pygame(fileName, pixelalpha=True)

def renderTiledSurface(tmxData):
    surface = pygame.Surface((tmxData.width * tmxData.tilewidth, tmxData.height * tmxData.tileheight))
    ti = tmxData.get_tile_image_by_gid
    for layer in tmxData.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = ti(gid)
                if tile:
                    surface.blit(tile, (x * tmxData.tilewidth, y * tmxData.tileheight))

    return surface
