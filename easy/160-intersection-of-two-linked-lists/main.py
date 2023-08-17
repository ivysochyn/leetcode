from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode
                            ) -> Optional[ListNode]:
        first = headA
        second = headB
        while first != second:
            first = headB if first is None else first.next
            second = headA if second is None else second.next
        return first


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
