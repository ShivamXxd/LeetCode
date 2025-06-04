# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itemList = []
        ptr = head
        while ptr:
            itemList.append(ptr.val)
            ptr = ptr.next
        itemList.sort()
        sortedHead = ListNode(itemList[0])
        temp = sortedHead
        for i in range(1, len(itemList)):
            temp.next = ListNode(itemList[i])
            temp = temp.next
        return sortedHead