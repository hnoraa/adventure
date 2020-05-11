from src.settings import *
from src.common import *
from .screenState import ScreenState


class MainScreen(ScreenState):
    def __init__(self, game):
        super().__init__(game, 'mainScreen')

        self.fontT = f_pygame_font.setupFont(FMONO, FXXL)
        self.textT = f_pygame_font.renderText(TITLE, self.fontT, CYAN)
        self.titleMidX = (self.textT.get_width() // 2)
        self.titleMidY = (self.textT.get_height() // 2)

    def events(self):
        super().events()

        if self.keys[pygame.K_RETURN]:
            # change state to main screen
            pass

    def update(self):
        super().update()

    def render(self):
        super().render()

        self.surface.fill(MAGENTA)

        self.game.screen.blit(self.surface, (0, 0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
