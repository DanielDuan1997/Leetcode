class Solution:
    def intToRoman(self, num: int) -> str:
        lst = list([['I', 'V'], ['X', 'L'], ['C', 'D'], ['M']])
        ret = ""
        for pos in range(3, -1, -1):
            x = num // 10**pos % 10
            if x <= 3:
                ret += lst[pos][0] * x
            elif 4 <= x <= 8:
                ret += lst[pos][0] * (x == 4) + lst[pos][1] + lst[pos][0] * max(0, x - 5)
            else:
                ret += lst[pos][0] + lst[pos + 1][0]
        return ret