# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1) # left = 0, right = mid - 1. So nums[mid] = middle element's previous
            root.right = helper(mid + 1, right) # mid element's right element
            # we create nodes of bst here with the helper function
            
            return root # returning the built up BST
        
        return helper(0, len(nums) - 1) # start from 0 and end so we get middle element as root.
