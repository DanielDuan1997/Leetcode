class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        f = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            f[i][i] = 1
            if i > 0:
                f[i][i - 1] = 1
        ans = n
        for l in range(2, n + 1):
            for le in range(n - l + 1):
                ri = le + l - 1
                if s[le] == s[ri]:
                    f[le][ri] = f[le + 1][ri - 1]
                ans += f[le][ri]
        return ans
