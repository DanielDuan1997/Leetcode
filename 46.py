class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        visit = [False] * n
        a = [0] * n
        
        def dfs(x):
            if x == n:
                ret.append(a.copy())
                return
            for i in range(n):
                if not visit[i]:
                    visit[i] = True
                    a[x] = nums[i]
                    dfs(x + 1)
                    a[x] = 0
                    visit[i] = False
        dfs(0)
        return ret
