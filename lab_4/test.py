from decorators1 import profile, memorize, convolve


@profile
@memorize
def main():
    for i in xrange(10 ** 6):
        a = 10


@convolve(2)
def mult2(x):
    return 2 * x

if __name__ == '__main__':
    main()
    main()
    print mult2(3)
