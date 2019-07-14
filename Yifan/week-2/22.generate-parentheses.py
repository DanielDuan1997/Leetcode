#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# n = 1 ()
# n = 2 ()() (())
# n = 3 ()()() ()(()) (())() (()()) ((()))


class Solution:
    def generateParenthesis(self, n: int):
        result = []
        for i in range(n):
            if not result:
                result.append('()')
                continue
            for s in result:
                if len(s) == 2 * (i):
                    for idx, c in enumerate(s):
                        if c == '(':
                            result.append(s[:idx + 1] + '()' + s[idx + 1:])
                    result.append(s + '()')
        final = set([s for s in result if len(s) == 2 * n])
        return list(final)


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
