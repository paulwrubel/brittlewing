from flower import Flower
import time
import pygame
from pygame import time, display, font


class Configuration:
    def __init__(self, screen_size: tuple[int, int], grid_size: tuple[int, int], framerate: int, flower_breed_period: float):
        # screen size
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.screen_size = screen_size
        self.center = self.width / 2, self.height / 2

        self.grid_size = grid_size
        self.framerate = framerate
        self.flower_breed_period = flower_breed_period

        self.flags = pygame.SCALED
        self.clock = time.Clock()
        self.screen = display.set_mode(screen_size, self.flags)
        self.font = font.SysFont("arial", 16)

        self.flowers: list[list[Flower]]
