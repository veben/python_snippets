from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list_node_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i, value in enumerate(values[1:], start=1):
        current.next = ListNode(value)
        current = current.next
        if i == pos:
            cycle_node = current

    if pos == 0:
        cycle_node = head

    if cycle_node:
        current.next = cycle_node

    return head


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True

        return False
