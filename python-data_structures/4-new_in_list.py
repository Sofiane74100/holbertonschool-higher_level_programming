#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    if idx < 0:
        return my_new_list
    if idx >= len(my_list):
        return my_new_list
    my_new_list[idx] = element
    return my_new_list
