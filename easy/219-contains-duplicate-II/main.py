from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = dict()
        for j, num in enumerate(nums):
            if (num in indexes and abs(j - indexes[num]) <= k):
                return True
            indexes[num] = j
        return False


if __name__ == "__main__":
    solver = Solution()
    print(solver.containsNearbyDuplicate([1, 2, 3, 1], 3), True)
    print(solver.containsNearbyDuplicate([1, 0, 1, 1], 1), True)
    print(solver.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)
