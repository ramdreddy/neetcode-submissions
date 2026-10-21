# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# seems p easy, go all the way down, return up, if diff > 1, return false
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(self, node):
            nonlocal res
            if not node:
                return 0
            lh = dfs(self, node.left)
            rh = dfs(self, node.right)
            if lh - rh > 1 or lh - rh < - 1:
                res = False
            return max(lh, rh) + 1
        dfs(self, root)
        return res