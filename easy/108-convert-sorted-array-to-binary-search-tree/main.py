from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def rec(nums, start, end):
            if start <= end:
                mid = (start + end) // 2
                node = TreeNode(nums[mid])
                node.left = rec(nums, start, mid - 1)
                node.right = rec(nums, mid + 1, end)
                return node
        return rec(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    solver = Solution()
    nums = [-10, -3, 0, 5, 9]
    print(solver.sortedArrayToBST(nums))

    nums = [1, 3]
    print(solver.sortedArrayToBST(nums))

    nums = [1, 3, 5]
    print(solver.sortedArrayToBST(nums))
