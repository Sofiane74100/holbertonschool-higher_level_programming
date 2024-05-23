#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_count += 1
        except (ValueError, TypeError):
            continue  # Skip non-integer values
        except IndexError:
            break  # Exit the loop if the index is out of range

    print()  # Print a newline at the end
    return printed_count
