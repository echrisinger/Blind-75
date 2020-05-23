class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        intervals.sort(key=lambda i: (i[0], -i[1]))
        s, e = intervals[0]
        
        res = []
        for new_s, new_e in intervals[1:]:
            if s <= new_s <= e:
                e = max(e, new_e)
            else:
                res.append([s, e])
                s, e = new_s, new_e
                
        res.append([s, e])
        return res

# O(nlogn) time, O(n) space

