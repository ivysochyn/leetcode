from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                k -= 1
        return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))
    print(nums)

    nums = [1]
    val = 1
    print(Solution().removeElement(nums, val))

    nums = [4, 5]
    val = 5
    print(Solution().removeElement(nums, val))

    nums = []
    val = 0
    print(Solution().removeElement(nums, val))
