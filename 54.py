import numpy as np
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        cur_dir = 0 if m > 1 else 1
        visited = []
        for i in range(n):
            visited.append([False] * m)
        x, y = 0, 0
        visited[x][y] = True
        ret = [matrix[x][y]]
        while True:
            nx = x + dx[cur_dir]
            ny = y + dy[cur_dir]
            if not (0 <= nx < n) or not (0 <= ny < m) or visited[nx][ny]:
                break
            while 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                x, y = nx, ny
                visited[x][y] = True
                ret += [matrix[x][y]]
                nx = x + dx[cur_dir]
                ny = y + dy[cur_dir]
            cur_dir = (cur_dir + 1) % 4
        return ret
