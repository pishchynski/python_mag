def get_pythagoras_triples(n):
    return [(x, y, z) for x in range(1, n + 1) for y in range(x, n + 1) for z in range(y, n + 1) if (
        z * z == x * x + y * y)]


if __name__ == '__main__':
    print(get_pythagoras_triples(100))
