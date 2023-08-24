from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for j, num in enumerate(nums):
            if j > k:
                seen.remove(nums[j - k - 1])
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solver = Solution()
    print(solver.containsNearbyDuplicate([1, 2, 3, 1], 3), True)
    print(solver.containsNearbyDuplicate([1, 0, 1, 1], 1), True)
    print(solver.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), False)
