class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = [[]]
        a = []
        def dfs(x):
            if x == n:
                return
            a.append(nums[x])
            ans.append(a.copy())
            dfs(x + 1)
            a.pop()
            for i in range(x, n):
                if nums[i] != nums[x]:
                    break
            if nums[i] != nums[x]:
                dfs(i)
        dfs(0)
        return ans
