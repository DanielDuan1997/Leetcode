class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0:
            return 0
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0:
            return 0
        f = [[0 for j in range(m)] for i in range(n)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0
        f[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    if i > 0:
                        f[i][j] += f[i - 1][j]
                    if j > 0:
                        f[i][j] += f[i][j - 1]
        return f[n - 1][m - 1]
