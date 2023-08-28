from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_depth(root):
            if not root:
                return 0
            left = calc_depth(root.left)
            right = calc_depth(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return calc_depth(root) != -1


if __name__ == '__main__':
    solver = Solution()
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(solver.isBalanced(tree), True)

    tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)),
                                TreeNode(3)), TreeNode(2))
    print(solver.isBalanced(tree), False)

    tree = TreeNode()
    print(solver.isBalanced(tree), True)
