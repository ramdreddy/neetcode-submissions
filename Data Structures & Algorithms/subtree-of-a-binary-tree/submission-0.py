# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            elif p.val != q.val:
                return False
            right = isSameTree(p.right, q.right)
            left = isSameTree(p.left, q.left)
            return left and right
        def dfs(root):
            if root == None:
                return False
            if root.val == subRoot.val:
                ans = isSameTree(root, subRoot)
                if ans == True:
                    return True
            return dfs(root.right) or dfs(root.left)
        return dfs(root)

        
        