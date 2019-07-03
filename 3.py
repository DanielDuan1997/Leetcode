class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        st = 0
        ret = 0
        for (ind, ch) in enumerate(s):
            last_pos = dct.get(ch, -1)
            dct[ch] = ind
            st = max(st, last_pos + 1)
            ret = max(ret, ind - st + 1)
        return max(ret, len(s) - st)
