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
        default=[10],
        help="Iterations count"
    )

    parser.add_argument(
        "-c", "--config",
        metavar="config_path",
        type=str, nargs=1,
        default=["config.json"],
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
        default=["output.txt"],
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


class CreatureConfig:
    def __init__(self, pred_life_period, pred_breed_period, prey_life_period, prey_breed_period):
        self.pred_life_period = pred_life_period
        self.pred_breed_period = pred_breed_period
        self.prey_life_period = prey_life_period
        self.prey_breed_period = prey_breed_period


creatureConfig = CreatureConfig(3, 2, -1, 2)


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
    def __init__(self, config_path='config.json', random=False):
        self.predators = []
        self.preys = []
        self.barriers = []
        self.size_x = 15
        self.size_y = 15

        self.read_config(config_path, random)

    @staticmethod
    def generate_map(size):
        return [[random.randint(BARRIER, PREY) for j in xrange(size[0])] for i in xrange(size[1])]

    def read_config(self, config_path, random_map):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

            creatureConfig.pred_life_period = config['pred_life_period']
            creatureConfig.pred_breed_period = config['pred_breed_period']
            creatureConfig.prey_life_period = config['prey_life_period']
            creatureConfig.prey_breed_period = config['prey_breed_period']

            if not random_map:
                ocean_map = config['map']
            else:
                map_size = config['map_size']
                ocean_map = self.generate_map(map_size)

            self.size_y = len(ocean_map)
            self.size_x = len(ocean_map[0])

            for y, line in enumerate(ocean_map):
                for x, cell in enumerate(line):
                    if int(cell) == PREDATOR:
                        self.predators.append(
                            Creature(x, y, PREDATOR, creatureConfig.pred_life_period, creatureConfig.pred_breed_period))
                    elif int(cell) == PREY:
                        self.preys.append(
                            Creature(x, y, PREY, creatureConfig.prey_life_period, creatureConfig.prey_breed_period))
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

    def check_move(self, creature, direction, is_child=False):
        if direction == 0:
            return True

        move = not ((creature.x + TURN[direction][0] < 0 or creature.x + TURN[direction][0] >= self.size_x) or (
            creature.y + TURN[direction][1] < 0 or creature.y + TURN[direction][1] >= self.size_y))

        if move:
            for barrier in self.barriers:
                move = not (
                    creature.x + TURN[direction][0] == barrier.x and creature.y + TURN[direction][1] == barrier.y)
                if not move:
                    break

        if move:
            for predator in self.predators:
                move = not (
                    creature.x + TURN[direction][0] == predator.x and creature.y + TURN[direction][1] == predator.y)
                if not move:
                    break

        if move and (creature.type == PREY or is_child):
            for prey in self.preys:
                move = not (
                    creature.x + TURN[direction][0] == prey.x and creature.y + TURN[direction][1] == prey.y)
                if not move:
                    break

        return move

    def __iterate_predator(self):
        for predator in self.predators:
            predator.breed_period -= 1
            if predator.breed_period == 0:
                predator.breed_period = creatureConfig.pred_breed_period

                breed_turn = random.randint(1, len(TURN) - 1)
                if not self.check_move(predator, breed_turn, True):
                    for i in range(1, len(TURN)):
                        birth_turn = ((i + breed_turn) % (len(TURN) - 1)) + 1
                        if self.check_move(predator, birth_turn, True):
                            self.predators.append(
                                Creature(predator.x + TURN[birth_turn][0], predator.y + TURN[birth_turn][1], PREDATOR,
                                         creatureConfig.pred_life_period, creatureConfig.pred_breed_period))
                            break
                else:
                    self.predators.append(
                        Creature(predator.x + TURN[breed_turn][0], predator.y + TURN[breed_turn][1], PREDATOR,
                                 creatureConfig.pred_life_period, creatureConfig.pred_breed_period))

            direction = random.randint(0, len(TURN) - 1)
            iter_limit = 100
            while not self.check_move(predator, direction):
                direction = random.randint(0, len(TURN) - 1)
                iter_limit -= 1
                if iter_limit == 0:
                    direction = 0
                    break

            predator.x += TURN[direction][0]
            predator.y += TURN[direction][1]
            prey = self.check_prey(predator.x, predator.y)
            if prey:
                predator.life_period = creatureConfig.pred_life_period
                self.preys.remove(prey)
            else:
                predator.life_period -= 1

            if predator.life_period == 0:
                self.predators.remove(predator)

    def __iterate_prey(self):
        for prey in self.preys:

            prey.breed_period -= 1
            if prey.breed_period == 0:
                prey.breed_period = creatureConfig.prey_breed_period

                breed_turn = random.randint(1, len(TURN) - 1)
                if not self.check_move(prey, breed_turn):
                    for i in range(1, len(TURN)):
                        birth_turn = ((i + breed_turn) % (len(TURN) - 1)) + 1
                        if self.check_move(prey, birth_turn, True):
                            self.preys.append(
                                Creature(prey.x + TURN[birth_turn][0], prey.y + TURN[birth_turn][1], PREY,
                                         creatureConfig.prey_life_period, creatureConfig.prey_breed_period))
                            break
                else:
                    self.preys.append(Creature(prey.x + TURN[breed_turn][0], prey.y + TURN[breed_turn][1], PREY,
                                               creatureConfig.prey_life_period, creatureConfig.prey_breed_period))

            direction = random.randint(0, len(TURN) - 1)
            iter_limit = 100
            while not self.check_move(prey, direction):
                direction = random.randint(0, len(TURN) - 1)
                iter_limit -= 1
                if iter_limit == 0:
                    direction = 0
                    break

            prey.x += TURN[direction][0]
            prey.y += TURN[direction][1]
            if prey.life_period > 0:
                prey.life_period -= 1
                if prey.life_period == 0:
                    self.preys.remove(prey)

    def iterate(self):
        first_turn = random.randint(PREDATOR, PREY)
        if first_turn == PREDATOR:
            self.__iterate_predator()
            self.__iterate_prey()
        else:
            self.__iterate_prey()
            self.__iterate_predator()

    def make_iterations(self, iterations_num):
        while iterations_num > 0 and len(self.predators) > 0 and len(self.preys) > 0:
            self.iterate()
            iterations_num -= 1

    def get_result(self, output_file):
        ocean_map = [['0' for j in range(self.size_x)] for i in range(self.size_y)]
        for predator in self.predators:
            ocean_map[predator.y][predator.x] = str(PREDATOR)
        for prey in self.preys:
            ocean_map[prey.y][prey.x] = str(PREY)
        for barrier in self.barriers:
            ocean_map[barrier.y][barrier.x] = str(BARRIER)

        with open(output_file, 'w') as out_f:
            for row in ocean_map:
                out_f.write(''.join(row) + '\n')


def main():
    args = parse_args()
    ocean = Map(args.config[0], args.random)
    ocean.make_iterations(args.iterations[0])
    ocean.get_result(args.output_file[0])
    return 0


if __name__ == '__main__':
    main()
