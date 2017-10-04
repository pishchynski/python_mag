def compress(sequence):
    return [(element, sequence.count(element)) for element in set(sequence)]


if __name__ == '__main__':
    print compress((1, 2, 1, 1, -4545))
