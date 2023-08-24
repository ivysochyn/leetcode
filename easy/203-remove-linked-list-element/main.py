from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode],
                       val: int) -> Optional[ListNode]:
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return head

        curr, prev = head.next, head
        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
                continue
            prev = curr
            curr = curr.next
        return head


if __name__ == "__main__":
    solver = Solution()
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(
        4, ListNode(5, ListNode(6)))))))
    val = 6
    result = solver.removeElements(head, val)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()

    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    val = 7
    result = solver.removeElements(head, val)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()
