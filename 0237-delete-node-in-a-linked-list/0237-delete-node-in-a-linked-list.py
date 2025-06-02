# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

class Solution:
    def deleteNode(self, node):
        nextNode = node.next
        node.val = nextNode.val
        node.next = nextNode.next