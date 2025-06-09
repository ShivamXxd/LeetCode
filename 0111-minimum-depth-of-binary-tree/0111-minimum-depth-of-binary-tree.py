# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def minDepth(root):
            if not root: # depth is 0 when root is absent
                return 0
            if not root.left and not root.right: 
                return 1 # depth is one if tree only has the root
            if not root.left: # if there's no left subtree, go to the right subtree and find shortest leaf node path
                return 1 + minDepth(root.right) # we add 1 cuz everytime we go deeper, depth increases
            if not root.right: # if there's no right subtree, do the same as prior with left subtree
                return 1 + minDepth(root.left)
            return 1 + min(minDepth(root.left), minDepth(root.right)) # find min of left and right subtree
        return minDepth(root)