"""
## Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

## Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

## Constraints:

`-231 <= n <= 231 - 1`
 

### Follow up: Could you solve it without loops/recursion?
"""


# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:

# print((-2**(31)) - 1)
# print((2**(31)) - 1)
# -2147483649
# 2147483647

numbers = [number for number in range(2147483650)]
print(numbers, file=open("numbers.txt", "a"))