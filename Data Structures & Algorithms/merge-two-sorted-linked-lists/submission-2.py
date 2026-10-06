# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        curr = ListNode(0, None)
        dummy = curr
        head1 = list1
        head2=list2
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = ListNode(head1.val, None)
                head1 = head1.next
            else:
                curr.next = ListNode(head2.val, None)
                head2 = head2.next
            curr = curr.next
        if head1:
            curr.next = head1
        elif head2:
            curr.next = head2
        else:
            return dummy.next
        return dummy.next
            
        
                
        

        