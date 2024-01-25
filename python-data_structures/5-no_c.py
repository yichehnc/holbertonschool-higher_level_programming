#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        new_string = ""
        for char in my_string:
            if char != "C" and char != "c":
                new_string = new_string + char
        return new_string
