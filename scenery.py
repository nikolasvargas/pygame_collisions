import random
from pygame import image, Rect, Surface
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL
from configparser import ConfigParser
from assets.colors import COLORS

_cfg = ConfigParser()
_cfg.read('game_config.ini')

SCREEN_WIDTH = int(_cfg['SCREEN']['WIDTH'])
SCREEN_HEIGHT = int(_cfg['SCREEN']['HEIGHT'])


class Cloud(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surf: Surface = image.load("assets/cloud.png").convert()
        self.surf.set_colorkey(COLORS['TRANSPARENT'], RLEACCEL)

        self.rect: Rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

    def update(self) -> None:
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Points(Sprite):
    def __init__(self) -> None:
        super().__init__()
