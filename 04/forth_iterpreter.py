# -*- coding:utf8 -*-

COMMANDS_LIST = (
    "PUT",
    "POP",
    "ADD",
    "SUB",
    "PRINT"
)


# parse command
def parse_command(line, line_number):
    command_line = line.rstrip().upper().split()
    command = {}
    key = ''
    value = False

    def parse_value(word):
        try:
            return int(word)
        except ValueError:
            try:
                return float(word)
            except ValueError:
                print "Error in line {0}, wrong value".format(line_number)


    if command_line[0] in COMMANDS_LIST:
        key = command_line[0]

        if len(command_line) > 1:
            value = parse_value(command_line[1])
            if value:
                return {key: value}
        else:
            return {key: False}
    else:
        print "Error in line {0}, skipping".format(line_number)
        return False


def eval_forth(file_name):
    file = open(file_name, "r")
    command_list = []
    data_stack = ()


    # parse file
    for line_number, line in enumerate(file):
        if line[0] == '#':
            pass
        else:
            command = parse_command(line, line_number)
            if command:
                command_list.append(command)

    print command_list


eval_forth("forth_programm.txt")