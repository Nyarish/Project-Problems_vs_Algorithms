# Explanation_3: Rearrange Array Digits

**Requirements:**

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.



**Approach:**

We know that given an array of integers between 0 to 9, find two numbers with maximum sum
formed by using all digits of the array. We know that a maximum number can be
formed from given digits (0-9) when the largest digit appears first, second
largest digit appears second, and so on.. finally the smallest digit appears
in the end.

The steps are as below:

Sort items in the array. To do this i shall;

1. Define a function `merge(left, right)` that takes as input two parts of an array [left, right], 
    and returnsa a merged list. 
2. Define a function `merge_sort(items)` that takes as input items of an array, 
    and then splits them into left and right, and finally returning a merged sorted list

3. Define a `rearrange_digits(input_list)` that rearranges array elements so as to form two number,
    such that thier sum is maximum, and finally returns Two maximum sums




**Complexity Analysis:**

*Time complexity:* `O(nlog(n))`

- Sorting: `O(nlog(n))` // for using mergesort
- 2-for loops: `O(n/2 + n/2)` => `O(n)` // iterating with the step-size of 2 makes it n/2
- Total: `O(nlogn + n)` => `O(nlog(n))`

*Space complexity:* `O(n)`

- Input space: `O(n)` where `n` is the length of input list
- Auxiliary space (extra or temporary space): `O(1)` // since we are reversing the sorted input in-place
- Total: Input space + Auxiliary space => `O(n + 1)` => `O(n)`