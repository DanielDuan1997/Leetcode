class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = []
        ret = []
        def dfs(x, left):
            if left == 0:
                ret.append(a.copy())
                return
            if left > n - x:
                return
            a.append(x + 1)
            dfs(x + 1, left - 1)
            a.pop()
            dfs(x + 1, left)
        dfs(0, k)
        return ret
