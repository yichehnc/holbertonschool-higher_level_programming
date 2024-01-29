#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    not_common_1 = list(filter(lambda x: x not in set_2, set_1))
    not_common_2 = list(filter(lambda x: x not in set_1, set_2))
    not_common_all = tuple(sorted(not_common_1 + not_common_2))
    return not_common_all
