
class Map:
    """
    It's our map with height of size_x and width of size_y.
    Cells have four states:
    -1 for barrier
     0 for free space
     1 for predator
     2 for victim
    """

    def __init__(self, size_x, size_y):
        self.__map = [[0 for _ in xrange(size_y)] for _ in xrange(size_x)]

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
