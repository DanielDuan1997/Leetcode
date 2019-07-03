class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        loop_len = 2 * numRows - 2
        s_len = len(s)
        ret = ""
        for row in range(numRows):
            for idx in range(row, s_len, loop_len):
                ret += s[idx]
                if 0 < row < numRows - 1 and idx + loop_len - 2*row < s_len:
                    ret += s[idx + loop_len - 2*row]
        return ret
