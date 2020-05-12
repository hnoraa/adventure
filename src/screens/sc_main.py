from src.common import *
from .screenState import ScreenState


class MainScreen(ScreenState):
    def __init__(self, game):
        super().__init__(game, 'mainScreen')

        # dimensions
        self.midX = (WIDTH // 2)
        self.midY = (HEIGHT // 2)

        # title
        self.fontT = f_pygame_font.setupFont(FMONO, FXXL)
        self.textT = f_pygame_font.renderText(TITLE, self.fontT, CYAN)
        self.titleMidX = (self.textT.get_width() // 2)
        self.titleMidY = (self.textT.get_height() // 2)

        # subtitle
        self.fontS = f_pygame_font.setupFont(FMONO, FXL)
        self.textS = f_pygame_font.renderText(SUBTITLE, self.fontS, LIMEGREEN)
        self.textSOffsetY = (self.textT.get_height())

    def events(self):
        super().events()

        if self.keys[pygame.K_RETURN]:
            # change state to main screen
            self.game.states.changeState('overworldScreen')

    def update(self):
        super().update()

    def render(self):
        super().render()

        self.surface.fill(MAGENTA)

        # show title
        f_pygame_font.drawText(self.surface, self.textT, self.midX - self.titleMidX, 0)

        # show subtitle
        f_pygame_font.drawText(self.surface, self.textS, self.midX - (self.textS.get_width() // 2), self.textSOffsetY)

        self.game.screen.blit(self.surface, (0, 0))

    def onEnter(self):
        super().onEnter()

    def onExit(self):
        super().onExit()
