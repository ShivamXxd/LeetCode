class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            total = 0
            if node.left: # check for left node
                if not node.left.left and not node.left.right: # check for leaf node
                    total += node.left.val
                else:
                    total += dfs(node.left) # check for such left leaves in node.left and add all into total
            total += dfs(node.right) # check same way for right side
            return total
        return dfs(root)