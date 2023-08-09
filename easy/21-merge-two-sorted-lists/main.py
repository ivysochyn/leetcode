from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while True:
            if not list2:
                current.next = list1
                break
            elif not list1:
                current.next = list2
                break

            if (list1.val > list2.val):
                current.next = ListNode(list2.val)
                list2 = list2.next
            else:
                current.next = ListNode(list1.val)
                list1 = list1.next
            current = current.next

        return head.next


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)
    while (merged):
        print(merged.val)
        merged = merged.next
