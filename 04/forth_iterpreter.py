# -*- coding:utf8 -*-

def forth(file_name):
    file = open(file_name, "r")

    data_stack = []
    commands_stack = ()

    for line in file:
        print line


forth("forth_programm.txt")