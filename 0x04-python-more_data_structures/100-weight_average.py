#!/usr/bin/python3

def weight_average(my_list=[]):
    return sum([n[0] * n[1] for n in my_list]) \
            / (sum([n[1] for n in my_list]) or 1)
