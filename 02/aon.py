

def decode(code):
    words = []
    result = []
    last_word = ''
    last_symbol = ''
    added_flag = False
    code_length = len(code)

    for i in range(code_length):
        if not added_flag:
            if code[i] == last_symbol:
                words.append(code[i])
                added_flag = True
            else:
                added_flag = False
        else:
            if code[i] != last_symbol:
                added_flag = False

        last_symbol = code[i]

    if '#' in words:
        # if # in result split list in chunks
        words = ''.join(words).split('#')
        last_word = words[-1]
        words = words[:-1]
        for word in words:
            # double last symbol in every substring
            result.append(word + word[-1:])
        result = ''.join(result) + last_word
    else:
        result = ''.join(words)

    return result


assert decode("") == ""
assert decode("1") == ""
assert decode("11") == "1"
assert decode("11111") == "1"
assert decode("11#") == "1"
assert decode("11##") == "11"
assert decode("11122234###55") == "1225"
assert decode("11122234###55##") == "12255"
assert decode("##11122234###55##") == "12255"