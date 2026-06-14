# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def inspector(node):
            if node is None:
                return 0
            
            left = inspector(node.left)
            right = inspector(node.right)

            if left == -1 or right == -1:
                return -1
            
            difference = left - right
            if difference > 1 or difference < -1:
                return -1
            
            maxheight = max(left, right)

            finalheight = maxheight + 1
            return finalheight

        result = inspector(root)
        if result == -1:
            return False
        else:
            return True
