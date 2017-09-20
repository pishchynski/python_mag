def get_sequence_item(k):
    res = 0
    for i in range(2 ** k):
        res = (res << 1) | (bin(i).count('1') % 2)

    return bin(res)
