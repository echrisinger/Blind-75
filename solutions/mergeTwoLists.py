# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        tail = head    
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    new_tail = l1
                    l1 = l1.next
                else:
                    new_tail = l2
                    l2 = l2.next
            elif not l2:
                new_tail = l1
                l1 = l1.next
            else:
                new_tail = l2
                l2 = l2.next
                
            new_tail.next = None
            tail.next = new_tail
            tail = new_tail
            
        return head

