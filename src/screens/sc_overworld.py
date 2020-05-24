from settings import *
from common import *
from .screenState import ScreenState


class OverworldScreen(ScreenState):
    def __init__(self, game):
        super().__init__(game, 'overworldScreen')

    def loadMap(self):
        # create surface
        self.mapE = TiledMap(mapsDir(OVERWORLD))
        self.mapImg = self.mapE.render()
        self.mapE.rect = self.mapImg.get_rect()

    def events(self):
        pass

    def events(self):
        super().events()

        if self.keys[pygame.K_p]:
            # change state to main screen
            self.game.states.changeState('pauseScreen')

    def update(self):
        super().update()

    def render(self):
        super().render()

        self.game.screen.blit(self.mapImg, (0, 0))

    def onEnter(self, reloadScreen=False):
        super().onEnter(reloadScreen)

        if reloadScreen:
            self.loadMap()

    def onExit(self):
        super().onExit()
