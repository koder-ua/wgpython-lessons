# -*- coding:utf8 -*-


def iterate_lines(fd):
    """
    получает имя файла итерирует по строкам. Для чтения можно использовать только fd.read(1)
    """
    file = open(fd, "r")
    char = file.read(1)
    file_line = ''

    while char != '':
        if char == '\n':
            yield file_line
            file_line = ''
        else:
            file_line += char
        char = file.read(1)

    yield file_line


def strip_spaces(iter):
    """
    принимает итератор, получает из него строки и возвращает строки без стартовых и финальных пробельных символов
    """
    for item in  iter:
        yield item.strip()


def drop_empty(iter):
    """
    получает итератор и возвращает только не пустые строки
    """
    for item in iter:
        if len(item) > 0:
            yield item


def split_items(iter):
    """
    получает итератор, считывает из него строки, разбивает их по пробелам и для каждого элемента определяет является ли
    он строковым представлением целого или числа с плавающей запятой. Приводит опознанные елементы к int/float
    соответсвенно, остальные оставляет строками. Возращает итератор по этим элементам
    """
    for item in iter:
        word_list = item.split(' ')
        for word in word_list:
            try:
                yield int(word)
            except ValueError:
                try:
                    yield float(word)
                except ValueError:
                    yield word



def get_ints(iter):
    """
    возращает из входного потока только целые
    """
    for item in iter:
        if isinstance(item, int):
            yield item


def my_sum(iter):
    """
    считает сумму элементов целых во входном потоке
    """
    return reduce(lambda x, y: x + y, iter)

file_name = "lorem.txt"


# assert list(iterate_lines(file_name)) == ["1 2 3 3.45 abra_cadabra   ", "", "12"]
assert list(strip_spaces(["1 2 3 3.45 abra_cadabra   ", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "", "12"]
assert list(drop_empty(["1 2 3 3.45 abra_cadabra", "", "12"])) == ["1 2 3 3.45 abra_cadabra", "12"]
assert list(split_items(["1 2 3 3.45 abra_cadabra", "12"])) == [1, 2, 3, 3.45, "abra_cadabra", 12]
assert list(get_ints([1, 2, 3, 3.45, "abra_cadabra", 12])) == [1, 2, 3, 12]
assert my_sum([1, 2, 3, 12]) == 18
assert my_sum(get_ints(split_items(drop_empty(strip_spaces(iterate_lines(file_name)))))) == 18