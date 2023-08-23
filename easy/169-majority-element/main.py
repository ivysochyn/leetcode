from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        count = 0

        for number in nums:
            if count == 0:
                answer = number
            if answer == number:
                count += 1
            else:
                count -= 1
        return answer


if __name__ == '__main__':
    solver = Solution()
    print(solver.majorityElement([3, 2, 3]), 3)
    print(solver.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
    print(solver.majorityElement([1]), 1)
