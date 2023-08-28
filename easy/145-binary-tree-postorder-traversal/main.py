from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, answer = [], []
        while stack or root:
            if root:
                stack.append(root)
                answer = [root.val] + answer
                root = root.right
            else:
                root = stack.pop().left
        return answer


if __name__ == '__main__':
    solver = Solution()
    tree = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(solver.postorderTraversal(tree), [3, 2, 1])
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    print(solver.postorderTraversal(tree), [2, 3, 1])
    tree = TreeNode(1, None, TreeNode(2))
    print(solver.postorderTraversal(tree), [2, 1])
    tree = TreeNode(1, TreeNode(2))
    print(solver.postorderTraversal(tree), [2, 1])
