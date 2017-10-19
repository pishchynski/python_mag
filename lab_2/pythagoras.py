def get_pythagoras_triples(n):
    """
    Retrieve all Pythagoras triples of numbers x, y, z such as x^2 + y^2 == z^2; 1 <= x <= n, 1 <= y <= n, 1 <= z <= n
    :param n: int
    :return: list of threes-tuples
    """
    return [(x, y, z) for x in range(1, n + 1) for y in range(x, n + 1) for z in range(y, n + 1) if (
        z * z == x * x + y * y)]
