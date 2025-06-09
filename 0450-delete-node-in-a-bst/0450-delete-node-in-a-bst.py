# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: # if we reach None then we didn't find the key so return None
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key) # delete from the left subtree and set it to the new subtree with the deleted node
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # if key == root.val 
            if not root.left: #  if there's no left subtree, return the right subtree with new tree root being its root
                return root.right
            if not root.right:
                return root.left
            
            successor = root.right # if the node has two children go to the right subtree
            while successor.left: # get to the leftmost node
                successor = successor.left # find the inorder successor and assign its value to the 'to be deleted' node's place
            root.val = successor.val # assign the inorder successor as its the replacer  
            root.right = self.deleteNode(root.right, successor.val) # delete the inorder successor so it doesn't repeat and assign the new subtree to root.right
        return root # return the new tree

        