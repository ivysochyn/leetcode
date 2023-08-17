from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.value = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        runner = head.next
        while True:
            if id(head) == id(runner):
                return True
            if runner is None or runner.next is None:
                return False
            head = head.next
            runner = runner.next.next


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
    head.next.next.next.next = head.next
    print(solution.hasCycle(head), True)

    head = ListNode(1, ListNode(2))
    head.next.next = head
    print(solution.hasCycle(head), True)

    head = ListNode(1)
    print(solution.hasCycle(head), False)

    head = None
    print(solution.hasCycle(head), False)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(solution.hasCycle(head), False)
