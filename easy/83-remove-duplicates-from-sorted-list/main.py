from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev, curr = head, head.next
            while curr:
                if curr.val == prev.val:
                    prev.next, curr = curr.next, curr.next
                else:
                    prev, curr = curr, curr.next
        return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(Solution().deleteDuplicates(head))

    head = ListNode(1, ListNode(1, None))
    print(Solution().deleteDuplicates(head))

    head = ListNode(1, ListNode(1, ListNode(1, ListNode(
        2, ListNode(3, ListNode(3))))))
    print(Solution().deleteDuplicates(head))

    head = None
    print(Solution().deleteDuplicates(head))

    head = ListNode(1, None)
    print(Solution().deleteDuplicates(head))
