import itertools
import os


def get_base(number):
    if number.startswith("0b"):
        return 2
    elif number.startswith("0o"):
        return 8
    elif number.startswith("0x"):
        return 16
    else:
        return 10


def multiply(first, second):
    if isinstance(first, str):
        base = get_base(first)

        try:
            first = int(first, base)
        except ValueError:
            return None

    if isinstance(second, str):
        base = get_base(second)

        try:
            second = int(second, base)
        except ValueError:
            return None

    result = first * second

    return result


def scalar_product(first, second):
    result = None

    try:
        result = sum(itertools.imap(multiply, first, second))
    except TypeError:
        result = None

    return result


def flatten(iterable):
    for item in iterable:
        if isinstance(item, str):
            yield item
        else:
            try:
                iterator = iter(item)

                for elem in flatten(iterator):
                    yield elem
            except TypeError:
                yield item


def listdir(node):
    cwd = os.getcwd()
    for item in os.listdir(cwd):
        try:
            os.chdir(cwd + "/" + item)
            d = os.getcwd().split("/")[-1]
            node[item] = {}
            listdir(node[item])
        except:
            node[item] = "file"


def walk_files(path):
    tree = {}
    path = path.rstrip(os.sep)
    start = path.rfind(os.sep) + 1

    for root, dirs, files in os.walk(path):
        subdirs = path[start:].split(os.sep)
        for subdir in subdirs:
            tree = tree[subdir]

            if dirs:
                for directory in dirs:
                    tree[directory] = {}
            else:
                tree[subdir] = files

    return tree


if __name__ == '__main__':
    print walk_files('D:\\distr')
