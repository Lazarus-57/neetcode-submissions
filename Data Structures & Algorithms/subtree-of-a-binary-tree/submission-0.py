# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False  # Main tree is empty, so subRoot can't be in it
        
        # 1. If the current nodes match, verify if the entire trees match
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. If they don't match, search for subRoot in the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        # If both are empty, they are identical
        if node1 is None and node2 is None:
            return True
        # If one is empty and the other isn't, or values don't match, they aren't identical
        if node1 is None or node2 is None or node1.val != node2.val:
            return False
        
        # Check if both left and right children are identical
        return self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)
        


