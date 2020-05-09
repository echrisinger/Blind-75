# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
                if fast and slow.val == fast.val:
                    return True
        
        return False
            
