from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


if __name__ == "__main__":
    solv = Solution()
    print(solv.singleNumber([4, 1, 2, 1, 2]), 4)
    print(solv.singleNumber([2, 2, 1]), 1)
    print(solv.singleNumber([1]), 1)
    print(solv.singleNumber([]), 0)
