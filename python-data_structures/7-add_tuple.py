#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_zero = 0
    b_zero = 0
    a_one = 0
    b_one = 0

    if len(tuple_a) >= 1 and tuple_a[0] is not None:
        a_zero = tuple_a[0]

    if len(tuple_a) >= 2 and tuple_a[1] is not None:
        a_one = tuple_a[1]

    if len(tuple_b) >= 1 and tuple_b[0] is not None:
        b_zero = tuple_b[0]

    if len(tuple_b) >= 2 and tuple_b[0] is not None:
        b_one = tuple_b[1]

    new_tuple = ((a_zero + b_zero), (a_one + b_one))
    
    return new_tuple
