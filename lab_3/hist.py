import sys


def distribute(dataset, k, visual_max_len=20):
    """
    Counts histogram for given dataset.

    :param dataset: iterable
    :param k: int number of parts
    :param visual_max_len: max number of asterisks to represent histogram. Default: 20. Ignored if <= 0.
    :return: list
    """

    min_elem = min(dataset)
    max_elem = max(dataset)
    hist = [0] * k

    if min_elem == max_elem:
        hist[0] = len(dataset)
        return hist

    for element in dataset:
        hist[min(int(k * (element - min_elem) / (max_elem - min_elem)), k - 1)] += 1
    if visual_max_len > 0:
        coef = max(hist) // visual_max_len + 1

    for length in hist:
        for _ in xrange(length // coef):
            sys.stdout.write('*')
        print

    return hist
