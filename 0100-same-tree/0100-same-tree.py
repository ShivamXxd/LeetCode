# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if not inorder(p.left, q.left):
                return False
            if p.val != q.val:
                return False
            if not inorder(p.right, q.right):
                return False
            return True

        return inorder(p, q)
