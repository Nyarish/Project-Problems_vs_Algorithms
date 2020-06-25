# Explanation_2: Search in a Rotated Sorted Array

**Requirement:**

Given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

Given a target value to search. If found in the array return its index, otherwise return -1.

We can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example: Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`



**Approach:**

Here are the steps i used to solve the problem:
        Step 1: Use Binary search function since it has a Time complexity of O (logn) for search
        Step 2: Get pivot function for input array using the Binary search for sorted and rotated array

Thus i find a pivot element (using binary search) such that there are two sorted arrays. Then check in which array does the target element reside. Then apply Binary Search on that array to find its position.


**Complexity Analysis:**

*Time complexity:* is `O(log(n))`

- Finding pivot => `O(logn)` // uses BinarySearch
- Binary search => `O(logn)`
- Total: `O(logn + logn)` => `O(log(n))`

*Space complexity:* is `O(n)`

- Input space: `O(n)` // array input
- Auxiliary space (extra or temporary space): `O(n)` // for sorted array
- Total: Input space + Auxiliary space => `O(n + n)` => `O(n)`