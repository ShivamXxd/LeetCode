# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        start = head
        dummy = ListNode(0)
        dummy.next = head
        prev_left = dummy
        for _ in range(left - 1):
            prev_left = prev_left.next
        start = prev_left.next

        prev = None
        current = start
        for _ in range(right - left + 1):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        prev_left.next = prev
        start.next = current

        return dummy.next
