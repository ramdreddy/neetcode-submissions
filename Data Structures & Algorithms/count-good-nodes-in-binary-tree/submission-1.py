# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        cmax = root.val
        def dfs(root, cmax):
            if not root:
                return
            if root.val >= cmax:
                self.ans+=1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, cmax)
                dfs(root.right, cmax)
        dfs(root,cmax)
        return self.ans


