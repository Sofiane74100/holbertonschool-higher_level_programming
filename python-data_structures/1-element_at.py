#!/usr/bin/python3
def element_at(my_list, idx):
    return my_list[idx]

my_list = [1, 2, 3, 4, 5]
idx = 3
element = element_at(my_list, idx)
print(f"Element at index {idx} is {element}")
