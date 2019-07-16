class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(arr):
            myset = set()
            for item in arr:
                if item == '.':
                    continue
                if item in myset:
                    return False
                myset.add(item)
            return True
        def get_arr(x, y):
            ret = []
            for i in range(3):
                for j in range(3):
                    ret.append(board[x * 3 + i][y * 3 + j])
            return ret
        for j in range(9):
            arr = []
            for i in range(9):
                arr.append(board[i][j])
                if not check(arr):
                    return False
        for i in range(9):
            arr = []
            for j in range(9):
                arr.append(board[i][j])
                if not check(arr):
                    return False
        for i in range(3):
            for j in range(3):
                if not check(get_arr(i, j)):
                    return False
        return True
