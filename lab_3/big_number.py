
def find_all(number, subnum):
    start = 0
    res = []
    while True:
        start = number.find(subnum, start)
        if start == -1:
            return res
        res.append(start + 1)
        start += 1


def index(number, subnums, max_len=5):
    if isinstance(subnums, int):
        subnums = (subnums,)
    index = []
    for subnum in subnums:
        index += find_all(number, str(subnum))
    return len(index), sorted(index)[:max_len]
