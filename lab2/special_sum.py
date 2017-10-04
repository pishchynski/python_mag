def calculate_special_sum(n):
    return sum([i * (i + 1) for i in range(1, n)])


if __name__ == '__main__':
    print(calculate_special_sum(1))
    print(calculate_special_sum(2))
    print(calculate_special_sum(3))
