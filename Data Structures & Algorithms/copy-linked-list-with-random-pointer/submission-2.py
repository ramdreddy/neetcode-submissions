"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ans = dict()
        curr = head
        while(curr):
            copy = Node(curr.val)
            ans[curr] = copy
            curr = curr.next
        curr = head
        while(curr):
            n = ans[curr]
            if(curr.next):
                n.next = ans[curr.next]
            else:
                n.next = None
            if(curr.random):
                n.random = ans[curr.random]
            else:
                n.random = None
            curr = curr.next
        return ans[head]
        