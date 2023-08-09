from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if (list1.val > list2.val):
            head = ListNode(list2.val)
            list2 = list2.next
        else:
            head = ListNode(list1.val)
            list1 = list1.next

        current = head

        while (list1 or list2):
            if (list1 and list2):
                if (list1.val > list2.val):
                    current.next = ListNode(list2.val)
                    list2 = list2.next
                else:
                    current.next = ListNode(list1.val)
                    list1 = list1.next
                current = current.next
            elif (list1):
                current.next = list1
                break
            else:
                current.next = list2
                break
        return head


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)
    while (merged):
        print(merged.val)
        merged = merged.next
