# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0

        def calculate_height(node):
            if node is None:
                return 0

            left = calculate_height(node.left)
            right = calculate_height(node.right)

            current_diameter = left + right

            self.max_diameter = max (current_diameter, self.max_diameter)

            return 1 + max(left, right)
        
        calculate_height(root)
        return self.max_diameter