#!/usr/bin/pyton3
def new_in_list(my_list, idx, element):
    """Replace element in a cpy list at specified pos."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cpy = [i for i in my_list]
    cpy[idx] = element
    return (cpy)
