class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end, descending, start descending.
        intervals.sort(key=lambda i: (i[1], -i[0]))
        max_interval_end = -1 * float('inf')
        erased = 0
        for i in intervals:
            if i[0] < max_interval_end:
                erased += 1
            else:
                max_interval_end = i[1]
                
        return erased
    
