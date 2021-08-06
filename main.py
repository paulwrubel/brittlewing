from flower import Flower, Species
from genome import Genome
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

    config.flowers[2][4] = Flower(Species.ROSE, Genome("rrggbbwwxx"), 0.05)
    config.flowers[3][5] = Flower(Species.ROSE, Genome("RrGgBbWwXx"), 0.05)
    config.flowers[4][6] = Flower(Species.ROSE, Genome("RRGGBBWWXX"), 0.05)
    config.flowers[5][7] = Flower(Species.ROSE, Genome("RrggBBwwXX"), 0.05)

    config.elapsed_ftime = 0
    config.breed_attempts = 0

    print("running main loop...")
    while True:
        loop(config)


def loop(config: Configuration):
    tick_time = config.clock.tick(config.framerate)
    config.elapsed_ftime += tick_time * 0.001

    check_events(config)
    config.screen.fill(WHITE)
    draw_grid(config)

    config.screen.blit(config.font.render(
        "FPS: {}".format(str(int(config.clock.get_fps()))), True, BLACK), (0, 0))
    config.screen.blit(config.font.render(
        "Breed Attempts: {}".format(str(config.breed_attempts)), True, BLACK), (0, 0))

    if config.elapsed_ftime >= config.flower_breed_period:
        config.elapsed_ftime = 0
        try_breed_flowers(config)
        config.breed_attempts += 1

    for x, flower_list in enumerate(config.flowers):
        for y, flower in enumerate(flower_list):
            if flower is not None:
                # print(x, y, flower)
                genome = flower.genome.short()
                variant = FLOWER_MAP[flower.species][flower.genome.short()]

                config.screen.blit(config.font.render(
                    "{} is {}".format(genome, variant), True, BLACK), (x*150, y*50))

    display.flip()


def try_breed_flowers(config: Configuration):
    for x, flower_list in enumerate(config.flowers):
        for y, flower in enumerate(flower_list):
            if flower is not None:
                n_x, n_y = get_rand_occupied_neighbor(config, (x, y))
                if n_x != -1 and n_y != -1:
                    n_flower = config.flowers[n_x][n_y]
                    if flower.species == n_flower.species and random.random() < flower.breed_chance:
                        e_x, e_y = get_rand_empty_neighbor(config, (x, y))
                        if e_x != -1 and e_y != -1:
                            config.flowers[e_x][e_y] = Flower(
                                flower.species, flower.genome.cross(n_flower.genome), flower.breed_chance)


def get_rand_occupied_neighbor(config: Configuration, location: tuple[int, int]) -> tuple[int, int]:
    neighbor_locations = get_neighbor_locations(config, location)
    occupied_neighbor_locations = list(filter(
        lambda n: config.flowers[n[0]][n[1]] is not None, neighbor_locations))

    if len(occupied_neighbor_locations) == 0:
        return (-1, -1)
    else:
        return random.choice(occupied_neighbor_locations)


def get_rand_empty_neighbor(config: Configuration, location: tuple[int, int]) -> tuple[int, int]:
    neighbor_locations = get_neighbor_locations(config, location)
    empty_neighbor_locations = list(filter(
        lambda n: config.flowers[n[0]][n[1]] is None, neighbor_locations))

    if len(empty_neighbor_locations) == 0:
        return (-1, -1)
    else:
        return random.choice(empty_neighbor_locations)


def get_neighbor_locations(config: Configuration, location: tuple[int, int]):
    x = location[0]
    y = location[1]
    possible_locs = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y),
                     (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]

    locs = filter(lambda loc:
                  loc[0] >= 0 and
                  loc[0] < config.grid_size[0] and
                  loc[1] >= 0 and
                  loc[1] < config.grid_size[1],
                  possible_locs)

    return locs


def draw_grid(config: Configuration):
    grid_width = int(config.screen_size[0] / config.grid_size[0])
    grid_height = int(config.screen_size[1] / config.grid_size[1])
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
    grid_size = (8, 12)
    framerate = 144
    flower_breed_period = 0.5
    return Configuration(screen_size, grid_size, framerate, flower_breed_period)


if __name__ == "__main__":
    start()
