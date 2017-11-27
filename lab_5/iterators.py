
def unique(iterable):
    result = set()
    for item in iterable:
        if item not in result:
            yield item
            result.add(item)


def transpose(matrix):
    return map(list, zip(*matrix))


if __name__ == '__main__':
    # res = unique([1, 2, 1, 3])
    # print(list(res))
    print transpose([[1, -1], [2, 3]])

