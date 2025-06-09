class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def inorder(node, count):
            nonlocal max_depth 
            if not node:
                max_depth = max(max_depth, count)
                return
            inorder(node.left, count + 1) # count increases as the depth increases
            inorder(node.right, count + 1)
        inorder(root, 0)
        return max_depth
