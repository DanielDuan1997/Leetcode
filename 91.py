import numpy as np
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = np.zeros(n, dtype=np.int)
        for i in range(n):
            if s[i] != '0':
                f[i] = f[i-1] if i else 1
            if i and (s[i-1] == '1' or (s[i-1] == '2' and s[i] in [str(j) for j in range(7)])):
                f[i] += f[i-2] if i > 1 else 1
        return f[n-1]
