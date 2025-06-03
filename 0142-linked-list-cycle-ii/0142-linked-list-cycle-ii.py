# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        seen = set()
        while ptr:
            if ptr not in seen:
                seen.add(ptr)
            else: 
                return ptr
            ptr = ptr.next
        return None