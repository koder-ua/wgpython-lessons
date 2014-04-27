# -*- coding:utf8 -*-

def my_pow(x):
    return x ** 2


def map_rq(func, iter):
    if len(iter) == 1:
        return [func(iter[0])]
    else:
        return [func(iter[0])] + map_rq(func, iter[1:])


def map_yield(func, iter):
    for item in iter:
        yield func(item)


def map_rq_yield(func, lst):
    if lst:
        # yield iter
        yield func(lst[0])
        for i in map_rq_yield(func, lst[1:]):
            yield i


print "a", map_rq(my_pow, [1, 2, 3])
print "b", list(map_yield(my_pow, [1, 2, 3]))
print "c", list(map_rq_yield(my_pow, [1, 2, 3]))