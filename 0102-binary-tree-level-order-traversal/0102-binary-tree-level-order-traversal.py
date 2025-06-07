# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root]) # store the root node in it
        result = [] # contains all levels
        while dq:
            level = [] # every level's nodes will be saved
            for _ in range(len(dq)):
                node = dq.popleft() # pop from left cuz we want nodes from left to right
                level.append(node.val) # add in current level

                if node.left: # if there is left child then add it in queue
                    dq.append(node.left) # we popped the root but left and right child nodes will be in queue
                if node.right: 
                    dq.append(node.right)
                # we added child nodes in queue and traverse through it popping them and adding in current level till queue is empty
            result.append(level)
        return result    
