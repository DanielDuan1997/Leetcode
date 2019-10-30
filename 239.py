from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        ret = []
        que = deque()
        for i in range(k):
            while len(que) > 0 and nums[que[-1]] < nums[i]:
                que.pop()
            que.append(i)
        ret.append(nums[que[0]])
        for i in range(k, len(nums)):
            while len(que) > 0 and nums[que[-1]] < nums[i]:
                que.pop()
            while len(que) > 0 and i - que[0] >= k:
                que.popleft()
            que.append(i)
            ret.append(nums[que[0]])
        return ret
