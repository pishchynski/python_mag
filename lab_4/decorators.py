import timeit


def memorize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if not kwargs:
            arguments = args
            if arguments not in cache:
                cache[arguments] = func(*args)
            return cache[arguments]
        else:
            return func(*args, **kwargs)

    return wrapper


def profile(f):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        f(*args, **kwargs)
        end_time = timeit.default_timer()
        print("Execution duration: {:.6f}s".format(end_time - start_time))

    return wrapper


def convolve(k):
    assert k > 0, "k must be positive!"

    def wrapper(func):
        def wrapped(*args):
            result = args
            for i in xrange(k):
                if not isinstance(result, tuple):
                    result = (result,)
                result = func(*result)
            return result

        return wrapped

    return wrapper
