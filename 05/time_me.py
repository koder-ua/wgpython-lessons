# -*- coding:utf8 -*-

import time

statistic = {}

def time_me():


@time_me(time.time, statistic)
def some_func(x, y):
    time.sleep(1.1)


time_me(1, 2)
time_me(1, 2)

