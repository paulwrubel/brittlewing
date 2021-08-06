from enum import Enum, auto

from constants import *
from genome import *


class Species(Enum):
    ROSE = auto()


class Variant(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

    CYAN = auto()
    YELLOW = auto()

    PINK = auto()
    PURPLE = auto()

    WHITE = auto()
    BLACK = auto()
    GREY = auto()

    RAINBOW = auto()
    GLITTER = auto()


VARIANT_MAP = {
    Variant.RED: RED
}


class Flower:
    def __init__(self, species: str, genome_string: str, breed_chance: float):
        self.species = species
        self.genome = genome_string
        self.breed_chance = breed_chance
