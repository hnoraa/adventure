from src.settings import *
from .screenState import ScreenState


class OverworldScreen(ScreenState):
    def __init__(self, game):
        super().__init__(game, 'overworldScreen')

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

        self.surface.fill(BEIGE)

        self.game.screen.blit(self.surface, (0, 0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
