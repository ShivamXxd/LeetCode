class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        second = head

        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        for _ in range(k-1):
            first = first.next
        for _ in range(length-k):
            second = second.next
        
        first.val, second.val = second.val, first.val
        return head