class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot & 1:
            return False
        n = len(nums)
        m = tot // 2
        f = [False] * (m + 1)
        f[0] = True
        for i in range(n):
            for j in range(m, nums[i] - 1, -1):
                f[j] |= f[j - nums[i]]
        return f[m]
