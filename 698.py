class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        target = sum(nums) // k
        if target * k != sum(nums): return False
        group_sum = [0] * n
        groups = 0
        def dfs(x):
            nonlocal groups
            if x == n: return True
            for i in range(groups):
                if group_sum[i] + nums[x] <= target:
                    group_sum[i] += nums[x]
                    if dfs(x + 1):
                        return True
                    group_sum[i] -= nums[x]
            if groups < k:
                groups += 1
                group_sum[groups - 1] = nums[x]
                if dfs(x + 1):
                    return True
                groups -= 1
            return False
        nums.sort()
        if nums[-1] > target: return False
        nums.reverse()
        return dfs(0)
