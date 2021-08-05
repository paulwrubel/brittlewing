import sys
import pygame
import math
from pygame import time, display, draw, font
from pygame.math import Vector2
from configuration import *


def start():
    print("starting brittlewing...")
    print(pygame.version)
    pygame.init()

    print("initializing configuration...")
    config = initialize_config()

    print("{0} x {1}".format(config.width, config.height))


def initialize_config():
    # create config
    screen_size = (500, 500)
    framerate = 144
    config = Configuration(screen_size, framerate, pygame.SCALED)

    config.clock = time.Clock()
    config.screen = display.set_mode(config.size, config.flags)
    config.font = font.SysFont("arial", 20)

    return config


if __name__ == "__main__":
    start()
