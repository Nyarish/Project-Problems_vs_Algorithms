# Explanation_1: Square Root of An Integer

**Requirement:**

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is `27`, the answer would be 5 because `sqrt(5) = 5.196` whose floor value is 5.

The expected time complexity is `O(log(n))`

**Summary:**

**Naïve Approach:** 

To find the floor of the Square Root, i shall try with all natural numbers starting from 1. Continue to increment the number by 1 until the product of the that number with itself is greater than input number.

Complexity Analysis:

- *Time complexity* => `O(sqrt(n))`
- *Space complexity:*
  - Input space => `O(1)`
  - Auxiliary space => `O(1)`
  - Total space => `O(1 + 1)` => `O(2)` => `O(1)`

**Optimized Approach:**

In the Naïve approach, we are trying to find square root of a number by multiplying a natural number by itself (starting from 1, increment by 1). This was further optimized using Binary Search Algorithm.

Complexity Analysis:

- *Time complexity:* `O(log(n))` as the time-complexity is dominated by BinarySearch
- *Space complexity:*
  - Input space: `O(1)` as input is a constant (integer)
  - Auxiliary space (extra or temp): `O(1)` 
  - Total space: `O(1 + 1)` => `O(2)` => `O(1)`