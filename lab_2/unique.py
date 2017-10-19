def compress(sequence):
    return [(element, sequence.count(element)) for element in set(sequence)]
