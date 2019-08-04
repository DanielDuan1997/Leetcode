class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        first_col = False
        for i in range(n):
            if not matrix[i][0]:
                first_col = True
            for j in range(1, m):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for j in range(m):
                matrix[0][j] = 0
        if first_col:
            for i in range(n):
                matrix[i][0] = 0
