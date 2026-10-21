# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ## how can i measure diameter in a bt
        ## for every root, we can measure max downward path and upward path
        ## run depth on both sides, and add is o(n^2)
        ## get to bottom and then return height up
        res = 0
        def moddfs(self, node):
            nonlocal res
            if not node:
                return 0
            leftside = moddfs(self, node.left)
            rightside = moddfs(self, node.right)
            res = max(res, leftside + rightside)
            return max(leftside, rightside) + 1
        moddfs(self, root)
        return res




        