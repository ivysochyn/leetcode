from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            curr_item = nums[mid]
            if curr_item == target:
                return mid
            elif curr_item > target:
                end = mid - 1
            else:
                start = mid + 1
        return end + 1


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    solution = Solution()
    print(solution.searchInsert(nums, target), 2)

    target = 7
    print(solution.searchInsert(nums, target), 4)

    target = 2
    print(solution.searchInsert(nums, target), 1)

    target = 0
    print(solution.searchInsert(nums, target), 0)
