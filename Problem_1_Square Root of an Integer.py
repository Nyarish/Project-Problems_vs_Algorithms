#!/usr/bin/env python
# coding: utf-8

# In[1]:



def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
       
       
    Complexity:
    Time complexity: O(logn)
    Space complexity:
        Input space: O(1)
        Auxiliary space (extra or temp): O(1)
        Total space: O(1 + 1) => O(2) => O(1)
       
       
    """
    
    # Handle Edge cases where number is a negative 
    if number < 0:
        return None
    
    if (number == 0 or number == 1):
        return number
    
    # perform Binary search for sqrt(number)
    start = 1
    end = number
    
    while start <= end:
        
        # Get midpoint
        mid = (start + end) // 2
        
        # if midpoint is a square return value
        
        if (mid * mid) == number:
            return mid
        
        # Since we need floor, we update the answer when mid*mid is smaller than number, 
        # and move closer to sqrt(number)
        
        if (mid * mid) < number:
            start = mid + 1
            ans = mid
        
        else:
            # if (mid * mid) > number
            end = mid - 1
            
            
    return ans

# Test 1
print('Test 1')
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Test 2
print('Test 2: Negative Numbers ')
print("Pass" if (None == sqrt(-25)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")

# References:
# https://github.com/suhassrivats
# https://www.geeksforgeeks.org/square-root-of-an-integer/
# https://github.com/suhassrivats


# In[ ]:




