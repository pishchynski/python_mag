def get_sequence_item(k):
    res = 0
    for i in range(k):
        bias = (1 << (1 << i))
        res = res * bias + (~res & (bias - 1))

    return bin(res)
