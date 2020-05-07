# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue()
        for i, l in enumerate(lists):
            if l:
                queue.put((l.val, i, l))
        
        if not queue.qsize():
            return None
        
        print(queue.queue)
        _, first_list_index, first_node = queue.get()
        replacement = first_node.next
        lists[first_list_index] = replacement
        if replacement:
            queue.put((replacement.val, first_list_index, replacement))
        
        head = first_node
        res = head
        head.next = None
        
        while queue.qsize():
            _, curr_list_index, curr_node = queue.get()
            replacement = curr_node.next
            lists[curr_list_index] = replacement
            if replacement:
                queue.put((replacement.val, curr_list_index, replacement))
            
            curr_node.next = None
            head.next = curr_node
            head = head.next
        
        return res
