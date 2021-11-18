from time import time, sleep
from functools import wraps
from numpy import nan


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


class ProgressBar:
    def __init__(self, target: int, resolution: int = 100, length: int = 20, sign: str = '\u2586'):
        self.__progress = 0
        self.__time = 0
        self.__step = max(1, target // resolution)
        self.target = target
        self.resolution = resolution
        self.length = length
        self.sign = sign

    def start(self):
        self.__time = time()

    def __update_time(self):
        self.__time = time() - self.__time

    def get_time(self, update: bool = False) -> float:
        if update:
            self.__update_time()
        return self.__time

    def remaining_time(self) -> float:
        try:
            return self.get_time() * (self.resolution / self.__progress - 1)  # TODO Timer too fast ?
        except ZeroDivisionError:
            return nan

    def __str__(self) -> str:
        empty_space = int((self.resolution - self.__progress) / self.resolution * self.length)
        try:
            remaining_time = time.strftime('%H:%M:%S', time.gmtime(self.remaining_time()))
        except ValueError:
            remaining_time = 'NaN'
        return '[' + self.sign * (self.length - empty_space) + ' ' * empty_space + '] {:.2f} % '.format(self.__progress / self.resolution * 100) + \
               'Remaining: ' + remaining_time

    def update(self, count: int, prt: bool = False):
        if (count % self.__step) == 0:
            self.__update_time()
            self.__progress = count / self.target * self.resolution
            if prt:
                print('\r' + self.__str__(), end='')


if __name__ == '__main__':
    @time_me(' ')
    def test(n):
        sleep(n)

    test(3)
    test(1)
