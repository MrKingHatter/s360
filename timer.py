from time import time, sleep
from functools import wraps


def time_me(end: str = '\n'):
    """
    Convience decorator with arguments to time the decorated method
    Arguments:
        end: The string to end the message with
    """
    message = '{name:} took {timing:.2f}s'

    def __time_me(f):
        @wraps(f)
        def wrap(*args):
            t = time()
            result = f(*args)
            print(message.format(name=f.__name__, timing=time() - t), end=end)
            return result
        return wrap
    return __time_me


if __name__ == '__main__':
    @time_me(' ')
    def test(n):
        sleep(n)

    test(3)
    test(1)
