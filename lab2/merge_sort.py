def merge(l_array, r_array):
    merge_array = []

    while l_array and r_array:
        if l_array[-1] > r_array[-1]:
            merge_array.append(l_array.pop())
        else:
            merge_array.append(r_array.pop())

    return (merge_array + l_array + r_array)[::-1]


def sort(array):
    if len(array) < 2:
        return array

    mid_index = len(array) // 2
    result = merge(list(sort(array[:mid_index])),
                   list(sort(array[mid_index:])))
    return result if isinstance(array, list) else tuple(result)