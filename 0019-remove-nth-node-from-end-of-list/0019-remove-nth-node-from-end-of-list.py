# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        prev = None
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        ptr = prev
        if n == 1:
            prev = prev.next
        else:
            for _ in range(n - 2):
                ptr = ptr.next
            ptr.next = ptr.next.next
        currentNode = prev
        newPrev = None
        while currentNode:
            next_node = currentNode.next
            currentNode.next = newPrev
            newPrev = currentNode
            currentNode = next_node
        return newPrev