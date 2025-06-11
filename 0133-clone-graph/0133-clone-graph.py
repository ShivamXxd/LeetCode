"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}  # this will keep track of the nodes that are already cloned
        def dfs(node):
            if not node:
                return None  # None if the input graph is empty
            if node in old_to_new:  # if node is already in old_to_new, it means its cloned already and we dont need to clone it again and just return it so itll be added to the neighbors list  
                return old_to_new[node]
            copy = Node(node.val)  # make the clone
            old_to_new[node] = copy  # add the clone to the tracker 

            for i in node.neighbors:
                copy.neighbors.append(dfs(i))  # add all neighbors in copy's neighbors using dfs 
            return copy
        return dfs(node)
