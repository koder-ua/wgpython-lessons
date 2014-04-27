import time

statistic = {}


def time_me(time_func, statistic):
    statistic["num_calls"] = 0
    statistic["cum_time"] = 0

    def decorator(fn):
        def wrapper(*args):
            call_start_time = time_func()
            result = fn(*args)
            call_end_time = time_func()
            statistic["cum_time"] += call_end_time - call_start_time
            statistic["num_calls"] += 1
            return result

        return wrapper

    return decorator


@time_me(time.time, statistic)
def some_func(x, y):
    time.sleep(1.1)


some_func(1, 2)
some_func(1, 2)

print statistic

assert statistic['num_calls'] == 2
assert 2.5 > statistic['cum_time'] > 2