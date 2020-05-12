from queue import PriorityQueue

class Solution:
    """
    ideas:
    store the k most frequent in a min heap, pop the smallest if the current count is greater
    O(n + n log(k))
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        for n in nums:
            counts[n] += 1
        
        vals = counts.items()
        pq = PriorityQueue()
        for n, count in vals:
            if k != 0:
                pq.put((count, n))
                k -= 1
            elif count > pq.queue[0][0]:
                pq.get()
                pq.put((count, n))
        
        return [n for _, n in pq.queue]


class Solution2:
    """
    ideas:
    store the k most frequent in a min heap, pop the smallest if the current count is greater
    O(n + n log(k))
    
    iterating through counts will always be O(n), as there will be less or eq counts to len(nums)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        for n in nums:
            counts[n] += 1
        
        count_items = defaultdict(list)
        for n, count in counts.items():
            count_items[count].append(n)
            
        res = []
        for count in range(len(nums), 0, -1):
            for n in count_items[count]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res
            
        

