"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    if len(input_array) <= 1:
        if input_array[0] == value:
            return 0
        else:
            return -1
        
    l, r = 0, len(input_array)-1

    while r-l > 1:
        m  = int(l+ (r-l)/2)
        
        if input_array[m] == value:
            return m
        
        if input_array[m] > value:
            r = m
        
        if input_array[m] < value:
            l = m
    

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))