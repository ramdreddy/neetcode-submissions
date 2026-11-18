# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## idea go up, return height
##

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def diameter(node):
            nonlocal res
            if not node:
                return 0
            lh = diameter(node.left)
            rh = diameter(node.right)
            res = max(res, lh + rh)
            return max(lh, rh) + 1
        diameter(root)
        return res






        