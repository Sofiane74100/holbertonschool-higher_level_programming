#!/usr/bin/python3
def delete_at(my_list=[], idx=3):
    if idx < len(my_list):
        del my_list[idx]
    return my_list
