from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for index, num in enumerate(nums):
            if num % 2 == 0:
                nums.insert(0, num)
                nums.pop(index)
        else:
            print(nums)


if __name__ == "__main__":
    soln = Solution()