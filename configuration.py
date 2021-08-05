from flower import Flower
import time
import math
from pygame import time, display, draw, font
from pygame.math import Vector2


class Configuration:
    def __init__(self, screen_size: tuple[int, int], framerate: int, flags: int):
        # screen size
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.size = screen_size
        self.center = self.width / 2, self.height / 2

        self.framerate = framerate

        self.clock = time.Clock()
        self.screen = display.set_mode(screen_size, flags)
        self.font = font.SysFont("arial", 16)

        self.flowers: list[Flower]
