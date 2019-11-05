class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums = [0, 1] + nums + [1]
        n += 2
        f = [[0 for j in range(n + 1)] for i in range(n + 1)]
        for l in range(3, n + 1):
            for le in range(1, n - l + 2):
                ri = le + l - 1
                for i in range(le + 1, ri):
                    f[le][ri] = max(f[le][ri], f[le][i] + f[i][ri] + nums[le] * nums[i] * nums[ri])
        return f[1][n]
