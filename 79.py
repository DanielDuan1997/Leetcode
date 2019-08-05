import numpy as np
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        len_word = len(word)
        visited = np.zeros((n, m), dtype=np.int16)
        def dfs(x, y, idx):
            if board[x][y] != word[idx]:
                return False
            if idx == len_word - 1:
                return True
            visited[x][y] = 1
            if x > 0 and not visited[x-1][y]:
                if dfs(x - 1, y, idx + 1):
                    return True
            if x < n - 1 and not visited[x+1][y]:
                if dfs(x + 1, y, idx + 1):
                    return True
            if y > 0 and not visited[x][y-1]:
                if dfs(x, y - 1, idx + 1):
                    return True
            if y < m - 1 and not visited[x][y+1]:
                if dfs(x, y + 1, idx + 1):
                    return True
            visited[x][y] = 0
            return False
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
