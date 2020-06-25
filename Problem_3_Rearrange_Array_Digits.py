#!/usr/bin/env python
# coding: utf-8

# In[2]:



# Define Helper functions

def merge(left, right):
    
    output = []
    left_idx = 0
    right_idx = 0
    
    """
    TODO:
        - Use while Loop to Traverse the lift until we have 1
        - If left items is larger, append right items then increament by 1, else
        append left items and increament by 1.
    """
    while left_idx < len(left) and right_idx < len(right):
        
        if left[left_idx] > right[right_idx]:
            output.append(right[right_idx])
            right_idx += 1
        else:
            output.append(left[left_idx])
            left_idx += 1
              
    """
    TODO:
        - Append any leftovers. Since we've broken from our while loop,
          we know at least one is empty, and the remaining:
             i) are already sorted
             ii) all sort past our last element in merged
    """
    
    output += left[left_idx:]
    output += right[right_idx:]
    
    return output


def merge_sort(items):
    
    # Base condition
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    
    left = items[:mid]
    right = items[mid:]
    
    # Call merge_sort recursively with the left and right half
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    x = 0
    y = 0
    
    sorted_item = merge_sort(input_list)[::-1]
    
    for i in range(0, len(sorted_item), 2):
        x = x * 10 + sorted_item[i]
        
    for j in range(1, len(sorted_item), 2):
        y = y * 10 + sorted_item[j]
        
    return [x, y]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print('Test 1')
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


print('Test 2 Edge cases')

test_function([[],[]])

print('Test 3 Edge cases')
test_function([[1],[1]])

# References:
# https://www.techiedelight.com/find-two-numbers-maximum-sum-array-digits/
# https://github.com/suhassrivats


# In[ ]:




