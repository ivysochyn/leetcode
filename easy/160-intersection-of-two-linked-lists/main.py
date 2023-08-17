from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode
                            ) -> Optional[ListNode]:
        nodes = {}
        while headA is not None:
            nodes[headA] = True
            headA = headA.next
        while headB is not None:
            if headB in nodes:
                return headB
            headB = headB.next
        return None


if __name__ == "__main__":
    solver = Solution()
    headA = ListNode(4, ListNode(1, ListNode(8, ListNode(4, ListNode(5)))))
    headB = ListNode(5, ListNode(0, ListNode(1, ListNode(8, ListNode(
        4, headA.next.next)))))
    print(solver.getIntersectionNode(headA, headB).val, 8)

    headA = ListNode(2, ListNode(6, ListNode(4)))
    headB = ListNode(1, ListNode(5))
    print(solver.getIntersectionNode(headA, headB), None)

    print(solver.getIntersectionNode(None, None), None)
