#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        ws = ' '
        sign = ['-', '+']
        number = [str(i) for i in range(10)]
        cons_ws = True
        cons_num = False
        cons_sign = True
        result_sign = 1
        result = []
        for i in range(len(s)):
            if s[i] == ws:
                if cons_num:
                    cons_ws = False
                if not cons_sign:
                    cons_ws = False
                continue
            if cons_ws:
                if s[i] in sign and cons_sign:
                    if cons_num:
                        cons_ws = False
                        continue
                    cons_sign = False
                    if s[i] == '-':
                        result_sign = -1
                    else:
                        result_sign = 1
                elif s[i] in number:
                    cons_num = True
                    result.append(s[i])
                else:
                    cons_ws = False
                continue
            if not cons_ws and not cons_num:
                return 0

        if not result:
            return 0
        #string to number
        ans = int(''.join(result)) * result_sign

        #check range
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN
        return ans


if __name__ == "__main__":
    s = Solution()
    ans = s.myAtoi("0-1")
    print(ans)
