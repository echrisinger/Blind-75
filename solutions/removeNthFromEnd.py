# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or (head.next == None and n == 1):
            return None
       
        behind = head
        ahead = head
        
        while n != 0:
            ahead = ahead.next
            n -= 1
        
        # if n is the length of the list, remove the first node
        if not ahead:
            return head.next
        
        # else traverse the list until behind is in front of node to remove
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
            
        behind.next = behind.next.next
        
        return head
    
