from queue import Queue
import numpy as np
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n:
            return []
        m = len(board[0])
        q = Queue()
        visited = np.zeros((n, m), dtype=np.int)
        def at_side(x, y):
            return x == 0 or x == n-1 or y == 0 or y == m-1
        def bfs(st_x, st_y):
            at_boarder = at_side(st_x, st_y)
            q = Queue()
            _q = Queue()
            q.put((st_x, st_y))
            _q.put((st_x, st_y))
            nonlocal visited
            visited[st_x][st_y] = True
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while not q.empty():
                x, y = q.get()
                for d in range(4):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    if board[nx][ny] == 'O':
                        at_boarder |= at_side(nx, ny)
                        q.put((nx, ny))
                        _q.put((nx, ny))
            if not at_boarder:
                while not _q.empty():
                    x, y = _q.get()
                    board[x][y] = 'X'
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if board[i][j] == 'O':
                    bfs(i, j)
