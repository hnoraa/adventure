from common import *
from .screenState import ScreenState


class PauseScreen(ScreenState):
    def __init__(self, game):
        super().__init__(game, 'pauseScreen')

        # dimensions
        self.midX = (WIDTH // 2)
        self.midY = (HEIGHT // 2)

        # title
        self.fontT = f_pygame_font.setupFont(FMONO, FXL)
        self.textT = f_pygame_font.renderText("Menu", self.fontT, CYAN)

    def events(self):
        super().events()

        if self.keys[pygame.K_SPACE]:
            # change state to main screen
            self.game.states.changeState(self.game.states.last.name)

    def update(self):
        super().update()

    def render(self):
        super().render()

        self.surface.fill(CORAL)

        # show title
        f_pygame_font.drawText(self.surface, self.textT, 10, 0)

        self.game.screen.blit(self.surface, (0, 0))

    def onEnter(self, reloadScreen=False):
        super().onEnter(reloadScreen)

    def onExit(self):
        super().onExit()
