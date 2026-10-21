# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ##return depth
        ##keep checking for 1 more, adding each time
        ##compare current with max?
        def dfs(self, root, num, res):
            if root:
                num +=1
                res = max(res, num)
                return max(dfs(self, root.left, num, res), dfs(self, root.right, num, res))
               
            else:
                return res
        num = 0
        res = 0
        return dfs(self, root, num, res)
            

        