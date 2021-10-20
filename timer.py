from time import time, sleep
from functools import wraps


def time_me(f: callable, end: str = '\n'):
    message = '{name:} took {timing:.2f}s'

    @wraps(f)
    def wrap(*args, **kwargs):
        t = time()
        result = f(*args, **kwargs)
        print(message.format(name=f.__name__, timing=time() - t), end=end)
        return result
    return wrap


if __name__ == '__main__':
    @time_me
    def test(n):
        sleep(n)

    test(3)
    test(1)
