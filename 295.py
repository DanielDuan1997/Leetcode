import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q0 = []
        self.q1 = []
        self.n0 = 0
        self.n1 = 0

    def addNum(self, num: int) -> None:
        if self.n0 == 0 or num > -self.q0[0]:
            heapq.heappush(self.q1, num)
            self.n1 += 1
            if self.n1 - 1 > self.n0:
                heapq.heappush(self.q0, -heapq.heappop(self.q1))
                self.n1 -= 1
                self.n0 += 1
        else:
            heapq.heappush(self.q0, -num)
            self.n0 += 1
            if self.n0 > self.n1:
                heapq.heappush(self.q1, -heapq.heappop(self.q0))
                self.n0 -= 1
                self.n1 += 1

    def findMedian(self) -> float:
        if self.n0 == self.n1:
            return (self.q1[0] - self.q0[0]) / 2
        else:
            return self.q1[0]
