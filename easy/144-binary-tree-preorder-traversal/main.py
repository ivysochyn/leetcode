from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        stack = []
        while True:
            while root:
                answer.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            if not stack:
                break
            root = stack.pop()
        return answer


if __name__ == "__main__":
    solver = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(solver.preorderTraversal(root), [1, 2, 3])

    root = TreeNode(1, TreeNode(2))
    print(solver.preorderTraversal(root), [1, 2])

    root = TreeNode(1, None, TreeNode(2))
    print(solver.preorderTraversal(root), [1, 2])
