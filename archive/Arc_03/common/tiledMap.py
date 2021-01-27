import pytmx
import pygame


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
