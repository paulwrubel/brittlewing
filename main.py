from flower import Flower, Species
import sys
import pygame
import math
import random
from pygame import time, display, draw, font
from pygame.math import Vector2
from flower_map import *

from configuration import *
from constants import *


def start():
    print("starting brittlewing...")
    print(pygame.version)
    pygame.init()

    print("initializing configuration...")
    config = initialize_config()

    print("initializing starting state...")
    config.flowers = []
    for x in range(8):
        config.flowers.append([])
        for _ in range(12):
            config.flowers[x].append(None)

    config.flowers[2][4] = Flower(Species.ROSE, "rrggbbwwxx")
    config.flowers[3][5] = Flower(Species.ROSE, "RrGgBbWwXx")
    config.flowers[4][6] = Flower(Species.ROSE, "RRGGBBWWXX")
    config.flowers[5][7] = Flower(Species.ROSE, "RrggBBwwXX")

    print("running main loop...")
    while True:
        loop(config)


def loop(config: Configuration):
    tick_time = config.clock.tick(config.framerate)

    check_events(config)
    config.screen.fill(WHITE)
    draw_grid(config)

    config.screen.blit(config.font.render(
        "FPS: {}".format(str(int(config.clock.get_fps()))), True, BLACK), (0, 0))

    try_breed_flowers(config)

    for x, flower_list in enumerate(config.flowers):
        for y, flower in enumerate(flower_list):
            if flower is None:
                continue

            # print(x, y, flower)
            genome = flower.genome.short()
            variant = FLOWER_MAP[flower.species][flower.genome.short()]

            config.screen.blit(config.font.render(
                "{} is {}".format(genome, variant), True, BLACK), ((x+1)*150, (y+1)*50))

    display.flip()


def try_breed_flowers(config):
    for x, flower_list in enumerate(config.flowers):
        for y, flower in enumerate(flower_list):
            if flower is None:
                continue
            n_x, n_y = get_first_neighbor(config, (x, y))
    if random.random() < 0.001:


def get_first_neighbor(config, location) -> tuple(int, int):
    neighbor_locations = []


def draw_grid(config: Configuration):
    grid_width = 150
    grid_height = 50
    for x in range(0, config.width, grid_width):
        for y in range(0, config.height, grid_height):
            rect = pygame.Rect(x, y, grid_width, grid_height)
            draw.rect(config.screen, BLACK, rect, 1)


def check_events(config: Configuration):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            temp = config.screen
            config.screen = display.set_mode(event.size, config.flags)
            config.screen.blit(temp, (0, 0))
            del temp


def initialize_config():
    # create config
    screen_size = (1200, 600)
    framerate = 144
    return Configuration(screen_size, framerate, pygame.SCALED)


if __name__ == "__main__":
    start()
