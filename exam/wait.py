# -*- coding:utf8 -*-

# Написать декоратор, реализующий случайную задержку перед вызовом декорируемой функции.

import time
import random


min_time = 2
max_time = 4


def wait(max_delay, min_delay):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            delay = min_delay + random.random() * (max_delay - min_delay)
            time.sleep(delay)
            return fn(*args, **kwargs)

        return wrapper

    return decorator


@wait(max_time, min_time)
def some_func():
    pass


start_time = time.time()
some_func()
duration1 = time.time() - start_time

start_time = time.time()
some_func()
duration2 = time.time() - start_time

assert duration1 != duration2
