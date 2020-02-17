# spriteSheet.py
# load images from a sprite sheet
import pygame

from . import f_pygame


class SpriteSheet:
    def __init__(self, fileName, scaleX=0, scaleY=0):
        # load the sprite sheet
        try:
            if scaleX == 0 and scaleY == 0:
                self.sheet = f_pygame.loadImage(fileName, False)
            else:
                self.sheet = f_pygame.loadScaledImage(fileName, scaleX, scaleY, False)
        except pygame.error as e:
            print(f"Unable to load sprite sheet image: {fileName}")
            raise SystemExit(e)
    
    def image_at(self, rectangle, colorKey = None):
        # load a specific image from a specific rectangle
        # loads from x, y, x+offset, y+offset
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()

        if colorKey is not None:
            if colorKey is -1:
                colorKey = image.get_at((0, 0))
            image.set_colorkey(colorKey, pygame.RLEACCEL)

        image.blit(self.sheet, (0, 0), rect)

        return image

    def images_at(self, rectangles, colorKey = None):
        # load a bunch of images, return a list
        return [self.image_at(rect, colorKey) for rect in rectangles]

    def load_strip(self, rectangle, imageCount, colorKey = None):
        # load a whole strip of images and return them as a list
        tuples = [(rectangle[0]+rectangle[2]*x, rectangle[1], rectangle[2], rectangle(3))
            for x in range(imageCount)]
            
        return self.images_at(tuples, colorKey)
