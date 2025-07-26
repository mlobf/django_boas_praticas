from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """times any functions"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = perf_counter()
        func(*args, **kwargs)
        end_time: float = perf_counter()
        total_time: float = round(end_time - start_time, 3)
        print(f'Times  {total_time}')

    return wrapper


@get_time
def do_something(param):
    sleep(1)
    for i in range(10**8):
        pass


if __name__ == '__main__':
    do_something('hello')
