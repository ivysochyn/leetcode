from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth, curr_depth = 0, 0
        stack = []
        while True:
            while root:
                curr_depth += 1
                if root.right:
                    stack.append((root.right, curr_depth))
                root = root.left
            depth = max(depth, curr_depth)
            if not stack:
                return depth
            root, curr_depth = stack.pop()


if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solver.maxDepth(root), 3)

    root = TreeNode(1, None, TreeNode(2))
    print(solver.maxDepth(root), 2)

    root = None
    print(solver.maxDepth(root), 0)
