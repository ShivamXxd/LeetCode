# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if not left and not right: # if both are None, it means theyre equal
                return True
            if not left or not right: # if one of them is None, then its not mirror
                return False
            if left.val != right.val: # compare for equal values
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
            # left subtree's left node should be equal to right subtree's right node for symmetry.
            # AND left subtree's right node should be equal to right subtree's left node for symmetry.
        if not root: # if the tree is empty, it is mirror of itself.
            return True
        return isMirror(root.left, root.right)
