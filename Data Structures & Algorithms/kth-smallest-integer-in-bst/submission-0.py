# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        def createlist(node):
            if node is None:
                return
            createlist(node.left)
            result.append(node.val)
            createlist(node.right)
        createlist(root)
        return result[k-1]