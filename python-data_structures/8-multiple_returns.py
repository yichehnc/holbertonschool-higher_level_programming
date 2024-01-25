#!/usr/bin/python3
def multiple_returns(sentence):
    str_length = 0
    first_char = None
    if sentence != '':
        str_list = list(sentence)
        str_len = len(str_list)
        first_char = str_list[0]

    return (str_len, first_char)
