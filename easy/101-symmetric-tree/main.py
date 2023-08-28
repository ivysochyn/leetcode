from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack_first = []
        stack_second = []
        curr_first, curr_second = root.left, root.right
        while True:
            while curr_first or curr_second:
                if ((not curr_first or not curr_second) or
                   (curr_first.val != curr_second.val)):
                    return False
                if curr_first.right and curr_second.left:
                    stack_first.append(curr_first.right)
                    stack_second.append(curr_second.left)
                elif curr_first.right or curr_second.left:
                    return False
                curr_first = curr_first.left
                curr_second = curr_second.right
            if not stack_first and not stack_second:
                return True
            elif not stack_first or not stack_second:
                return False
            curr_first = stack_first.pop()
            curr_second = stack_second.pop()


if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))
    print(solver.isSymmetric(root), True)

    root = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                    TreeNode(2, None, TreeNode(3)))
    print(solver.isSymmetric(root), False)
