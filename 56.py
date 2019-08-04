class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        intervals.sort(key=lambda x: x[0])
        for item in intervals:
            if not ret or ret[-1][1] < item[0]:
                ret.append(item)
            else:
                ret[-1][1] = max(ret[-1][1], item[1])
        return ret
