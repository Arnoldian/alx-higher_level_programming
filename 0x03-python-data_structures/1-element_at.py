#!/usr/bin/python3

def element_at(my_list, idx):
    if (idx < 0) | (idx > (len(my_list) - 1)):
        return (None)
    idx_num = my_list[idx]
    return (idx_num)
