class Solution:
    ret_len = 0
    ret = ""

    def updateLen(self, s, st, ed):
        if ed - st + 1 <= self.ret_len:
            return
        self.ret_len = ed - st + 1
        self.ret = s[st : ed + 1]

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        for i in range(s_len):
            evenHalfLen = min(i, s_len - 1 - i - 1)
            for j in range(evenHalfLen + 1):
                if s[i - j] != s[i + 1 + j]:
                    evenHalfLen = j - 1
                    break
            self.updateLen(s, i - evenHalfLen, i + 1 + evenHalfLen)

            oddHalfLen = min(i, s_len - 1 - i)
            for j in range(oddHalfLen + 1):
                if s[i - j] != s[i + j]:
                    oddHalfLen = j - 1
                    break
            self.updateLen(s, i - oddHalfLen, i + oddHalfLen)

        return self.ret
