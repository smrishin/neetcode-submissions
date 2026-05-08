from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []
        

    def addNum(self, num: int) -> None:
        heappush(self.minh, num)

        while len(self.minh) > len(self.maxh):
            heappush(self.maxh, -heappop(self.minh))
        
        while len(self.maxh) > len(self.minh):
            heappush(self.minh, -heappop(self.maxh))

    def findMedian(self) -> float:
        if len(self.minh) == len(self.maxh):
            return (self.minh[0] + -self.maxh[0]) / 2
        else:
            return self.minh[0]

        