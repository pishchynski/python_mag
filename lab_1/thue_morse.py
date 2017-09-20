def get_sequence_item(k):
    res = 0
    for i in range(2 ** k - 1):
        res = (res << i)
        if (i % 2 == 0):
            res = res + (~res & 1)
        else:
            res = (~res & 1)
        # print(bin(res))
    return bin(res)


if __name__ == '__main__':
    print(get_sequence_item(2))
