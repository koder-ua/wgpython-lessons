

def find_average(val1, val2, val3):

    if val1 < val2 < val3:
        return val2
    elif val3 < val2 < val1:
        return val2
    elif val1 < val3 < val2:
        return val3
    elif val2 < val3 < val1:
        return val3
    elif val2 < val1 < val3:
        return val1
    elif val3 < val1 < val2:
        return val1
    else:
        return 'error'


assert find_average(1, 2, 3) == 2
assert find_average(4, 2, 1) == 2
assert find_average(4, 5, 3) == 4
assert find_average(4, 2, 6) == 4
assert find_average(6, 2, 3) == 3
assert find_average(1, 4, 3) == 3
assert find_average(1, 4, 3) == 2


