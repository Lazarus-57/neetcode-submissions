# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  

        if p is None and q is None: #both trees hit the end at the same time
            return True
        elif p is None or q is None: #one tree abruptly ends
            return False
        elif p.val != q.val: #both nodes exist, but are not the same
            return False
            
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left and right:
            return True
        else:
            return False
