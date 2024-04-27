# """
# Explanation in the page:

# Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also
# the square of a palindrome.

# Given two positive integers left and right represented as strings, return the number of
# super-palindromes integers in the inclusive range [left, right].


# Example 1:
# - - - - -

# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

# Example 2:
# - - - - -
# Input: left = "1", right = "2"
# Output: 1


# Constraints:
# - - - - - -

# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 1018 - 1].
# left is less than or equal to right.
# """


from math import sqrt
from typing import List


class Solution:
    def is_palindrome(self, num: int) -> bool:
        num_ = str(num)

        if num_ == num_[::-1]:
            return True
        return False

    def is_an_square_number(self, num: int) -> tuple:
        if str(float(sqrt(num))).split(".")[-1] == "0":
            return (True, float(sqrt(num)))
        else:
            return (False, None)

    def generate_palindromic_numbers(self, left: int, right: int) -> List[int]:
        result = []
        for number in range(left, right + 1):
            if self.is_palindrome(number):
                result.append(number)
        else:
            return result

    def superpalindromesInRange(self, left: str, right: str) -> int:
        left_ = int(left) or None
        right_ = int(right) or None

        numbers = []
        total_palindromes = 0

        if left_ is not None and right_ is not None:
            if left_ >= 0 and right_ < ((10**18) - 1):
                if left_ <= right_:
                    numbers = self.generate_palindromic_numbers(left_, right_)

        for number in numbers:
            #
            # if the number is an square number need to get the square and check if both
            # are palindrome
            #
            number_and_truth = self.is_an_square_number(number)
            if number_and_truth[0]:
                # if self.is_palindrome(number):
                if self.is_palindrome(int(number_and_truth[1])):
                    total_palindromes += 1
                    print(
                        f"Palindrome: {number} | Square Of the Palindrome: {int(number_and_truth[1])}\nCurrent Count:{total_palindromes}\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= "
                    )

        return total_palindromes


a = Solution()
from time import perf_counter

# time_s = perf_counter()
# print(a.superpalindromesInRange("1","1000"))
# time_sp = perf_counter()

# print(f"Took time: {round(time_sp - time_s, 3)} s")


# time_s = perf_counter()
# print(a.superpalindromesInRange("1","10000"))
# time_sp = perf_counter()

# print(f"Took time: {round(time_sp - time_s, 3)} s")

time_s = perf_counter()
print(a.superpalindromesInRange("40000000000000000", "50000000000000000"))
time_sp = perf_counter()

print(f"Took time: {round(time_sp - time_s, 3)} s")
