import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
# heapq only provides minheap so if you want maxheap, multiply by -1

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, num*-1)
        heapq.heappush(self.right, heapq.heappop(self.left) * -1)

        # rebalance
        # also make sure if length is odd, the median value is just from the left heap
        if (len(self.right) > len(self.left)):
            heapq.heappush(self.left, -1*heapq.heappop(self.right))

    def findMedian(self) -> float:
        if (((len(self.left) + len(self.right)) % 2) == 1):
            return self.left[0] * -1
        else:
            return (self.left[0] * -1 + self.right[0]) / 2
        
        