def max_integer(my_list=[]):
    if not my_list:
        return None
    bigger = my_list[0]
    for number in my_list:
        if number > bigger:
            bigger = number 
            return bigger
