# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def compare(node1, node2):
            nonlocal res
            if not node1 and not node2:
                return
            elif not node1:
                res = False
                return
            elif not node2:
                res = False
                return
            if node1.val == node2.val:
                compare(node1.right, node2.right)
                compare(node1.left, node2.left)
            else:
                res = False
                return
        compare(p, q)
        return res
            
            
        