# f_pytmx.py
# functions to load and render tmx files
import pytmx
import pygame

from . import f_pygame


def loadTmxFromFile(fileName):
    """
    Loads a TMX file
    :param fileName: name/path of file
    :return: TMX object
    """
    return pytmx.load_pygame(fileName, pixelalpha=True)


def renderTiledSurface(tmxData):
    """
    Render the tiled surface
    :param tmxData: TMX object
    :return: rendered surface
    """
    surface = pygame.Surface((tmxData.width * tmxData.tilewidth, tmxData.height * tmxData.tileheight))
    ti = tmxData.get_tile_image_by_gid
    for layer in tmxData.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = ti(gid)
                if tile:
                    surface.blit(tile, (x * tmxData.tilewidth, y * tmxData.tileheight))

    return surface


def getObjCenter(tileObj):
    """
    Get the center of a tiled object
    :param tileObj: the tiled object
    :return: a vector for the center of the tiled object
    """
    return f_pygame.vec((tileObj.x + tileObj.width / 2), (tileObj.y + tileObj.height / 2))
