from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        This problem has two solutions:

        * Iterate over all elements with item and enumerator and apply XOR
        * This will work as XOR from equal numbers is 0
        > x = 0
        > for i, item in enumerate(nums):
        >    x ^= i ^ item
        > return x ^ len(nums)

        * Second approach is to calculate total sum of an arithmetic
        * progression, and subtract sum of a given array.
        """
        return int((len(nums) + 1) * len(nums) / 2) - sum(nums)


if __name__ == "__main__":
    solver = Solution()
    print(solver.missingNumber([3, 0, 1]), 2)
    print(solver.missingNumber([0, 1]), 2)
    print(solver.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
    print(solver.missingNumber([0]), 1)
