#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if type(my_list) == list:
        # reverse list
        my_list.reverse()
        # print reversed list
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
