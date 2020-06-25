#!/usr/bin/env python
# coding: utf-8

# In[1]:



# Get Helper function

def Binary_Search(start, end, input_arr, target):
    
    while start <= end:
        
        mid_point = (start + end) // 2
        
        if input_arr[mid_point] == target:
            return mid_point
        else:
            if input_arr[mid_point] > target:
                end = mid_point - 1
            else:
                start = mid_point + 1
    return -1


def get_Pivot_index(start, end, input_arr):
    
    mid_point = start + (end - start) // 2
    pivot_idx = 0
    
    # In case of Sorted array: mid_point + 1 would be greater than mid_point,
    # if Not, we found pivot_idx
    
    if input_arr[mid_point] > input_arr[mid_point + 1]:
        return mid_point + 1
    
    else:
        if input_arr[start] > input_arr[mid_point]:
            # It means that pivot is in right of mid
            pivot_idx = get_Pivot_index(start, mid_point - 1, input_arr)
        else:
            # It means that pivot is in left of mid
            pivot_idx = get_Pivot_index(mid_point + 1, end, input_arr)
    
    return pivot_idx



# Main program 

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Handle Edge cases where input is empty or has one element 
    
    if len(input_list) == 0:
        return -1
    
    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1
    
    start = 0
    end = len(input_list) - 1
    results = 0
    
    # Condition 1. If input_list is sorted perfom Binary search
    if input_list[start] < input_list[end]:
        
        results = Binary_Search(start, end, input_list, number)
    
    else:
        
        # Condition 2. If Not sorted get pivot 
        pivot_index = get_Pivot_index(start, end, input_list)
        
        # check where the number lies in the arrat
        # Check in the right sorted array
        if number >= input_list[pivot_index] and number <= input_list[end]:
            results = Binary_Search(pivot_index, end, input_list, number)
        else:
            # Check in the left sorted array
            results = Binary_Search(start, pivot_index -1, input_list, number)
    
    return results


# Test Functions

def linear_search(input_list, number):
    
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print('Test 1')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print('Test 2: Edge cases')
test_function([[], -1])

# References:
# https://www.youtube.com/watch?v=5BI0Rdm9Yhk


# In[ ]:




