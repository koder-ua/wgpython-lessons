# -*- coding:utf8 -*-

# Реализовать функцию flatten получающую на вход список, часть элементов которого
# могут быть списками или генераторами. flatten должна рекурсивно их раскрыть в одномерным
# массив. При этом список или генератор заменяется на свои элементы в оригинальном массиве.


def flatten(items):
    def list_items(elems):
        for item in elems:
            if hasattr(item, '__iter__'):
                for sub_item in flatten(item):
                    yield sub_item
            else:
                yield item

    return list(list_items(items))


assert flatten([1, iter([2, 3]), [2], 3]) == [1, 2, 3, 2, 3]
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([1, 2, [3]]) == [1, 2, 3]
assert flatten([[1, 2], [1, 3]]) == [1, 2, 1, 3]
assert flatten([[1, [[[[2]]]], [1, [3, [[[[[4]]]]]]]]]) == [1, 2, 1, 3, 4]