class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if len(s) == 0:
            return 0
        ret = 0
        positive = True
        if s[0] == '-':
            positive = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for ch in s:
            if '0' <= ch <= '9':
                ret = ret * 10 + int(ch)
            else:
                break
        if not positive:
            ret = -ret
        ret = min(ret, 2**31 - 1)
        ret = max(ret, -2**31)
        return ret
