import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = np.zeros((m, n))
        for j in range(n):
            f[0][j] = 1
        for i in range(1, m):
            f[i][0] = 1
            for j in range(1, n):
                f[i][j] = f[i][j - 1] + f[i - 1][j]
        return int(f[m - 1][n - 1])