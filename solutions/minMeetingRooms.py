import queue

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        q = queue.PriorityQueue()
        for start, end in intervals:
            q.put((start, 1))
            q.put((end, -1))
            
        count = 0
        max_count = 0
        while q.qsize():
            count += q.get()[1]
            max_count = max(max_count, count)
            
        return max_count
            
        

