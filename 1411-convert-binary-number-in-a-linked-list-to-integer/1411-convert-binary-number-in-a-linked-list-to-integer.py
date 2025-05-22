# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ptr = head
        binaryString = ""
        while ptr is not None:
            binaryString += str(ptr.val)
            ptr = ptr.next
        return int(binaryString, 2)