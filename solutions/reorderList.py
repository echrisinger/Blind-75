# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not (head and head.next):
            return head
        
        # slow is now at the last element of the final list, needs to be reversed
        second_half = self.removeSecondHalf(head)
        # head is now the first half
        reversed_second_half = self.reverseList(second_half)
        list1 = head
        list2 = reversed_second_half
        
        while list2:
            list2_head = list2
            list1_next = list1.next
            list2 = list2.next
            list2_head.next = list1_next
            list1.next = list2_head
            list1 = list1_next
        
    def removeSecondHalf(self, head: ListNode) -> ListNode:
        slow = fast = head
        slow_prev = None
        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        slow_prev.next = None
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        rev = None
        curr = head
        # 1 => 2 => 3
        while curr:
            curr_next = curr.next # 2 # 3 # None
            curr.next = rev # None # 2.next = 1 => None # 3.next = 2 => 1 => None
            rev = curr # 1 => None # 2 => 1 => None =
            curr = curr_next # 2 # 3
            
        return rev


