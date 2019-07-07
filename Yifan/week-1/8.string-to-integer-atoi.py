#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2*31 − 1
        INT_MIN = -2*31
        
        ws = ' '
        sign = ['-','+']
        number = [str(i) for i in range(10)]

        result = []
        for i in range(len(s)):
            if s[i] == ws:
                continue
            elif s[i] in number:
                result.append(s[i])
        #string to number
        ans=int(''.join(result))

        #check range
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:

if __name__ == "__main__":
    s = Solution()
    ans = s.myAtoi('123')
    print(ans)



