# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        prev = None
        ptr = head
        while ptr and ptr.next:
            first = ptr
            second = ptr.next

            first.next = second.next
            second.next = first

            if prev:
                prev.next = second
            
            prev = first
            ptr = first.next
        return new_head