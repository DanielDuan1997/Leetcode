#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


class Solution:
    def intToRoman(self, num: int) -> str:
        th = (num // 1000) * 'M'
        h = (num % 1000) // 100
        if h == 9:
            h = 'CM'
        elif h >= 5:
            h = 'D' + (h - 5) * 'C'
        elif h == 4:
            h = 'CD'
        else:
            h = h * 'C'
        t = (num % 100) // 10
        if t == 9:
            t = 'XC'
        elif t >= 5:
            t = 'L' + (t - 5) * 'X'
        elif t == 4:
            t = 'XL'
        else:
            t = t * 'X'
        s = num % 10

        if s == 9:
            s = 'IX'
        elif s >= 5:
            s = 'V' + (s - 5) * 'I'
        elif s == 4:
            s = 'IV'
        else:
            s = s * 'I'
        return th + h + t + s


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(444))
