# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = l1
        curr2 = l2
        s = str()
        s2 = str()
        while(curr):
            n = curr.val
            s = str(n) + s
            curr = curr.next
        while(curr2):
            n2 = curr2.val
            s2 = str(n2) + s2
            curr2 = curr2.next
        v1 = int(s)
        v2 = int(s2)
        value = v1 + v2
        value2 = str(value)
        head = None
        for i in range(len(value2)-1, -1, -1):
            if not head:
                head = ListNode(int(value2[i]))
                curr = head
            else:
                curr.next = ListNode(int(value2[i]))
                curr = curr.next
        return head

        
        
