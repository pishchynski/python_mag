import logging
import traceback
from contextlib import contextmanager


@contextmanager
def handle_error_context(re_raise=True, log_traceback=True, exc_type=Exception):
    try:
        yield None
    except exc_type as e:
        if log_traceback:
            logging.exception(traceback.format_exc())
        if re_raise:
            raise e


def handle_error(re_raise=True, log_traceback=True, exc_type=Exception):
    def wrapper(func):
        def inner(*args, **kwargs):
            with handle_error_context(re_raise, log_traceback, exc_type):
                func(*args, **kwargs)

        return inner

    return wrapper
