# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # nums = []  # This code includes equal node values which is not allowed for this question
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     nums.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return nums == sorted(nums)

        def dfs(node, low, high):
            if not node:  # return True if we reached a leaf node's left or right which is always None
                return True
            if not low < node.val < high: # if value is out of required bounds then it is not BST
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
            # when going left, current node is always gonna be highest value for all left nodes
            # when going right, current node is always gonna be lowest for all the right nodes
        return dfs(root, float("-inf"), float("inf"))