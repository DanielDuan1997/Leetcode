class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for str in strs:
            u = str.count('0')
            v = str.count('1')
            for i in range(m, u - 1, -1):
                for j in range(n, v - 1, -1):
                    f[i][j] = max(f[i][j], f[i - u][j - v] + 1)
        return f[m][n]
