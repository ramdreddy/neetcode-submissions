# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ### while list1 and list2, increment and store next as least
        ## once one runs out, set next to the one thats alive or else return
        dummy = ListNode(0)
        curr = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val, None)
                curr1 = curr1.next
                
            else:
                curr.next = ListNode(curr2.val, None)
                curr2 = curr2.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        elif curr2:
            curr.next = curr2
        return dummy.next
        