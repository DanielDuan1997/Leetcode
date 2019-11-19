class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        last = intervals[0][0]
        for i in range(n):
            if last <= intervals[i][0]:
                n -= 1
                last = intervals[i][1]
        return n
