# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ##what's happening in the invert
        ##probably use recursion
        ##just keep swapping l and r
        ##
        def invert(self, node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
            invert(self, node.right)
            invert(self, node.left)
        invert(self, root)
        return root


        