class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        a = []
        n = len(candidates)
        candidates.sort()
        def dfs(x, m):
            if m == 0:
                ret.append(a.copy())
                return
            if x == n or m < candidates[x]:
                return
            a.append(candidates[x])
            dfs(x, m - candidates[x])
            a.pop()
            dfs(x + 1, m)
        dfs(0, target)
        return ret
