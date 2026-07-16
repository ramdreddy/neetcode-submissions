# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        slow = head 
        fast = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        current = slow.next
        slow.next = None
        prev = None
        while(current):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        curr = head
        while(prev):
            temp1 = curr.next
            temp2 = prev.next
            curr.next = prev
            prev.next = temp1
            curr = temp1
            prev = temp2
            
        return 
