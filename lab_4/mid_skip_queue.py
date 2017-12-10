from collections import deque
from pprint import PrettyPrinter


class MidSkipQueue:
    def __init__(self, k, iterable=()):
        if k <= 0:
            raise ValueError("k must be positive")
        self.store_num = k
        self.head = list(iterable[:self.store_num])

        if len(iterable) >= 2 * self.store_num:
            tmp = iterable[-self.store_num:]
        else:
            tmp = iterable[self.store_num:]

        self.tail = deque(tmp, self.store_num)

    def __str__(self):
        pp = PrettyPrinter(indent=4)
        if len(self.tail) > 0:
            return pp.pformat(self.head)[:-1] + ' ... ' + pp.pformat(list(self.tail))[1:]
        else:
            return pp.pformat(self.head)

    def __eq__(self, other):
        return self.head == other.head and self.tail == other.tail

    def __len__(self):
        return len(self.head) + len(self.tail)

    def __getitem__(self, index):
        if isinstance(index, slice):
            assert index.start and index.stop, "incomplete slices are not supported"
            assert index.start >= 0 and index.stop >= 0, "indexes must be non-negative"

            start, stop = index.start, index.stop
            step = index.step if index.step else 1

            if start > self.store_num and stop > self.store_num:
                return [self.tail[i] for i in xrange(start - self.store_num, stop - self.store_num, step)]
            elif stop > self.store_num:
                if step < 0:
                    return [self.tail[i] for i in xrange(0, stop - self.store_num, step)] + self.head[start::step]
                else:
                    return self.head[start::step] + [self.tail[i] for i in xrange(0, stop - self.store_num, step)]
            else:
                return self.head[index]

        assert abs(index) < 2 * self.store_num, "wrong index"

        if index < 0:
            index = self.__len__() + index

        if index < self.store_num:
            return self.head[index]
        else:
            return self.tail[index - self.store_num]

    def __contains__(self, item):
        return self.index(item) != -1

    def __add__(self, other):
        new_queue = MidSkipQueue(self.store_num, self.head + list(self.tail))

        for item in other:
            new_queue.append(item)

        return new_queue

    def index(self, element):
        index = -1
        try:
            index = self.head.index(element)
            return index
        except ValueError:
            try:
                index = self.tail.index(element)
                return self.store_num + index
            except ValueError:
                return index

    def append(self, *args):
        for item in args:
            if len(self.head) != self.store_num:
                self.head.append(item)
            else:
                self.tail.append(item)


class MidSkipPriorityQueue(MidSkipQueue):
    def append(self, *args):
        temp = sorted(self.head + list(self.tail) + list(args))

        self.head = temp[:self.store_num]

        if len(temp) >= 2 * self.store_num:
            self.tail = temp[-self.store_num:]
        else:
            self.tail = temp[self.store_num:]

    def __add__(self, other):
        new_queue = self.head + list(self.tail) + list(other)
        return MidSkipPriorityQueue(self.store_num, sorted(new_queue))
