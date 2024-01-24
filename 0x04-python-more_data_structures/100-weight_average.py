#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    result = 0
    counter = 0
    for i, val in enumerate(my_list):
        result += val[0] * val[1]
        counter += val[1]
    return result / counter
