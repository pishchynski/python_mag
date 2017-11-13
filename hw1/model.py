import argparse
import json
import sys
import random


def parse_args():
    parser = argparse.ArgumentParser(
        description="Ocean life modelling",
        usage="model.py [-i] [-r] [-c <file>] [-o <file>]"
    )

    parser.add_argument(
        "-i", "--iterations",
        metavar="iterations",
        type=int, nargs=1,
        default=5,
        help="Iterations count"
    )

    parser.add_argument(
        "-c", "--config",
        metavar="config_path",
        type=str, nargs=1,
        default="./config.json",
        help="JSON config"
    )

    parser.add_argument(
        "-r", "--random",
        action="store_true",
        help="Generate map randomly"
    )

    parser.add_argument(
        "-o", "--output-file",
        metavar="output_file",
        type=str, nargs=1,
        default="./output.txt",
        help="Modelling result file path"
    )

    args = parser.parse_args(sys.argv[1:])
    return args


BARRIER = -1
FREE = 0
PREDATOR = 1
PREY = 2
TURN = ((0, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0))


class Creature:
    def __init__(self, x, y, type, life_period=3, breed_period=2):
        self.x = x
        self.y = y
        self.type = type
        self.life_period = life_period
        self.breed_period = breed_period


class Barrier:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Map:
    def __init__(self, config_path, random=False):
        self.predators = []
        self.preys = []
        self.barriers = []

        self.read_config(config_path, random)

    def read_config(self, config_path, random):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

            pred_life_period = config['pred_life_period']
            pred_breed_period = config['pred_breed_period']
            prey_life_period = config['prey_life_period']
            prey_breed_period = config['prey_breed_period']

            if not random:
                ocean_map = config['map']
            else:
                map_size = config['map_size']
                ocean_map = self.generate_map(map_size)

            for y, line in enumerate(ocean_map):
                for x, cell in enumerate(line):
                    if int(cell) == PREDATOR:
                        self.predators.append(Creature(x, y, PREDATOR, pred_life_period, pred_breed_period))
                    elif int(cell) == PREY:
                        self.preys.append(Creature(x, y, PREY, prey_life_period, prey_breed_period))
                    elif int(cell) == BARRIER:
                        self.barriers.append(Barrier(x, y))

    def check_prey(self, x, y):
        for prey in self.preys:
            if prey.x == x and prey.y == y:
                return prey
        return False

    def check_predator(self, x, y):
        for predator in self.predators:
            if predator.x == x and predator.y == y:
                return predator
        return False

    def check_move(self, creature, direction):
        move = not ((creature.x + TURN[direction][0] < 0 or creature.x + TURN[direction][0] >= self.x) or (
        creature.y + TURN[direction][1] < 0 or creature.y + TURN[direction][1] >= self.y))

        if move:
            for barrier in self.barriers:
                move = not (
                creature.x + TURN[direction][0] == barrier.x or creature.y + TURN[direction][1] == barrier.y)

        if move:
            for predator in self.predators:
                move = not (
                creature.x + TURN[direction][0] == predator.x or creature.y + TURN[direction][1] == predator.y)

        if move and creature.type == PREY:
            for prey in self.preys:
                move = not (
                creature.x + TURN[direction][0] == prey.x or creature.y + TURN[direction][1] == prey.y)

        return move

    def generate_map(self, size):
        return [[random.randint(-1, 2) for j in xrange(size[1])] for i in xrange(size[0])]

    def add_predator(self, x, y):
        self.__map[x][y] = 1

    def add_victim(self, x, y):
        self.__map[x][y] = 2

    def add_barrier(self, x, y):
        self.__map[x][y] = -1

    def get_cell(self, x, y):
        return self.__map[x][y]

    def move(self, x_start, y_start, x_dest, y_dest):
        if self.__map[x_start][y_start] not in (-1, 0) and self.__map[x_dest][y_dest] not in (-1, 1):
            self.__map[x_dest][y_dest] = self.__map[x_start][y_start]


class Predator:
    """
    It's a predator
    """

    def __init__(self, x, y, satiety):
