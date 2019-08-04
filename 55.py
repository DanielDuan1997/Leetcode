class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        maxpos = 0
        i = 0
        while i <= maxpos:
            nxtpos = i + nums[i]
            if nxtpos > maxpos:
                maxpos = min(n - 1, nxtpos)
                if maxpos == n - 1:
                    return True
            i += 1
        return False
