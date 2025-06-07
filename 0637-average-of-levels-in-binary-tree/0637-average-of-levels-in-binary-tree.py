# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from decimal import Decimal, getcontext
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return root
        getcontext().prec = 10
        dq = deque([root])
        result = []
        while dq:
            level_sum = 0
            count = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                level_sum += node.val
                count += 1
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            result.append(Decimal(level_sum / count))
        return result
        