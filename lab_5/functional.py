import itertools


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

