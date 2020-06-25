#!/usr/bin/env python
# coding: utf-8


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
       
       
    Complexity:
        Time complexity: O(n)
    Space complexity:
        Input space => O(n)
        Auxiliary space => O(1)
        Total space => O(n + 1) => O(n)
    """
    
    low_idx = 0
    mid = 0
    high_idx = len(input_list) - 1
    
    # Base condition
    while (mid <= high_idx):
        
        # if values is 0 perform a swap on the low and mid elements
        if input_list[mid] == 0:
            input_list[low_idx], input_list[mid] = input_list[mid], input_list[low_idx]
            
            low_idx += 1
            mid += 1
        # make 1 be the pole
        elif input_list[mid] == 1:
            
            mid += 1
        elif input_list[mid] == 2:
            # if values is 2 perform a swap on the high and mid elements
            input_list[high_idx], input_list[mid] = input_list[mid], input_list[high_idx]
            high_idx -= 1  
    
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

        
print('Test 1')        
print('For three-way partitioning the Test Assumes zero-based array ')       
print('______________________________________________________________')       

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print()

print('Test 2')

test_function([])


# References:
# https://www.youtube.com/watch?v=BOt1DAvR0zI
# https://en.wikipedia.org/wiki/Dutch_national_flag_problem#Pseudocode
# https://github.com/suhassrivats


