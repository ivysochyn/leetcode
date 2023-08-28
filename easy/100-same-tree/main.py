from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        while True:
            while p or q:
                if (not p or not q) or (p.val != q.val):
                    return False
                stack.append((p.right, q.right))
                p, q = p.left, q.left
            if not stack:
                break
            p, q = stack.pop()
        return False if p or q else True


if __name__ == "__main__":
    solution = Solution()
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solution.isSameTree(tree1, tree2), True)

    tree1 = TreeNode(1, TreeNode(2))
    tree2 = TreeNode(1, None, TreeNode(2))
    print(solution.isSameTree(tree1, tree2), False)

    tree1 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree2 = TreeNode(1, TreeNode(1), TreeNode(2))
    print(solution.isSameTree(tree1, tree2), False)
