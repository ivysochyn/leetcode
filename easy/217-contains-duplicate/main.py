from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == '__main__':
    solver = Solution()
    print(solver.containsDuplicate([1, 2, 3, 1]), True)
    print(solver.containsDuplicate([1, 2, 3, 4]), False)
    print(solver.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
    print(solver.containsDuplicate([]), False)
