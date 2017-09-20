if __name__ == '__main__':
    res_list = []
    for x in range(1, 51):
        res = ''
        if x % 3 == 0:
            res += 'Fizz'

        if x % 5 == 0:
            res += 'Buzz'
        res_list.append(res if res != '' else str(x))

    print(', '.join(res_list))
