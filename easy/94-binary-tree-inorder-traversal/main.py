from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + \
                self.inorderTraversal(root.right) if root else []


if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(solver.inorderTraversal(root), [1, 3, 2])

    root = TreeNode(1, TreeNode(2))
    print(solver.inorderTraversal(root), [2, 1])

    root = TreeNode(1, None, TreeNode(2))
    print(solver.inorderTraversal(root), [1, 2])

    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    print(solver.inorderTraversal(root), [3, 2, 1])
