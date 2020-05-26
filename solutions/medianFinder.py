from queue import PriorityQueue

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smaller = PriorityQueue()
        self.larger = PriorityQueue()

    def addNum(self, num: int) -> None:
        self.larger.put(num)
         
        if self.larger.qsize() - 1 > self.smaller.qsize() or\
           (self.smaller.qsize() and self.larger.queue[0] < -self.smaller.queue[0]):
            self.smaller.put(-self.larger.get())
        if self.larger.qsize() < self.smaller.qsize():
            self.larger.put(-self.smaller.get())

    def findMedian(self) -> float:
        if self.smaller.qsize() == self.larger.qsize():
            return ((-self.smaller.queue[0]) + self.larger.queue[0]) / 2
        return self.larger.queue[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

