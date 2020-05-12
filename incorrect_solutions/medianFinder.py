from queue import PriorityQueue

class MedianFinder:
    # this approach would work, if I didn't try to have one heap store all of 
    # the entries, and instead kept it balanced
    # inserting the larger half of the entries
    # into a min heap, and the smaller half into a max heap.
    # adding a new entry into the max heap, you pull off the new largest number (of the smaller half)
    # and insert into the min.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = PriorityQueue()
        self.max_heap = PriorityQueue()
        
    def addNum(self, num: int) -> None:
        if self.min_heap.qsize():
            self.min_heap.put(-num)
        else:
            self.max_heap.put(num)

    def findMedian(self) -> float:
        if not self.min_heap.qsize() and not self.max_heap.qsize():
            return 0
        
        if self.min_heap.qsize():
            active_heap, inactive_heap = self.min_heap, self.max_heap
        else:
            active_heap, inactive_heap = self.max_heap, self.min_heap
            
        num_to_remove = (active_heap.qsize() - inactive_heap.qsize()) // 2
        while num_to_remove != 0:
            inactive_heap.put(-active_heap.get())
            num_to_remove -= 1
            
        if self.max_heap.qsize() > self.min_heap.qsize():
            median = self.max_heap.queue[0]
        elif self.min_heap.qsize() > self.max_heap.qsize():
            median = -self.min_heap.queue[0]
        else:
            median = (-self.min_heap.queue[0] + self.max_heap.queue[0]) / 2
        
        while active_heap.qsize():
            inactive_heap.put(-active_heap.get())
            
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
