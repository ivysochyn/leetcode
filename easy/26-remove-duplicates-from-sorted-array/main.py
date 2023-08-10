from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))

    nums = [1, 1]
    print(Solution().removeDuplicates(nums))

    nums = [1, 1, 1]
    print(Solution().removeDuplicates(nums))

    nums = []
    print(Solution().removeDuplicates(nums))
