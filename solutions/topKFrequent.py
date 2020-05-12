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

