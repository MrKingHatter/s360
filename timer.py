from time import time, sleep
from functools import wraps


def time_me(f: callable, end: str = '\n'):
    message = '{name:} took {timing:.2f}s'

    @wraps(f)
    def __time_me(__f):
        def wrap(*args):
            t = time()
            result = __f(*args)
            print(message.format(name=__f.__name__, timing=time() - t), end=end)
            return result
        return wrap
    return __time_me


if __name__ == '__main__':
    @time_me('')
    def test(n):
        sleep(n)

    test(3)
    test(1)
