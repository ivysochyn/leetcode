from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


if __name__ == "__main__":
    solv = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = solv.reverseList(head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    head = ListNode(1, ListNode(2))
    head = solv.reverseList(head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

    head = None
    print(solv.reverseList(head))
