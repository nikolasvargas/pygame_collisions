import random
from pygame import Surface
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT


SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600


class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surf = Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.window_bounds = 0

    def _check_bounds(self) -> None:
        if self.rect.left < self.window_bounds:
            self.rect.left = self.window_bounds
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= self.window_bounds:
            self.rect.top = self.window_bounds
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, key: dict) -> None:
        if key[K_UP]:
            self.rect.move_ip(0, -5)
        if key[K_DOWN]:
            self.rect.move_ip(0, 5)
        if key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(5, 0)

        self._check_bounds()


class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.surf = Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20) * -1

    def update(self) -> None:
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()