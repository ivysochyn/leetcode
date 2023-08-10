from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current = nums[0]
        index = 0

        for i in range(1, len(nums)):
            if nums[i] != current:
                current = nums[i]
                index += 1
                nums[index] = current
        return index + 1


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
