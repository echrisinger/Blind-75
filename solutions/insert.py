class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_s, new_e = newInterval
        inserted = False
        
        for inter in intervals:
            s, e = inter
            if (new_s <= s <= new_e) or\
               (new_s <= e <= new_e) or\
               (s < new_s and e > new_e):
                new_s = min(new_s, s)
                new_e = max(new_e, e)
            else:
                if not inserted and s > new_e:
                    res.append([new_s, new_e])
                    inserted = True
                res.append([s, e])
            
        if not inserted:
            res.append([new_s, new_e])
        
        return res

# O(n) time, O(n) space -- ignoring res, O(1)
# If you wanted to make this true O(1) space,
# you could track the range of values to delete in intervals
# and after completed shift all values left into that range
# (that are right of that range) -- not sure how to 
# do that in Python.
# Then, insertion will also take O(n) time at the given index
# (first index after new start)
