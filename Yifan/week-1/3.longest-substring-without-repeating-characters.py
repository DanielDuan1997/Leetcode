#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        last_idx = 0
        for i in range(len(s)):
            if s[i] in s[last_idx:i]:
                if i-last_idx>max_len:
                    max_len = i-last_idx     
                last_idx = last_idx+s[last_idx:i].find(s[i])+1
                
        return max(max_len,i-last_idx+1)

# if __name__ == "__main__":
#     s = Solution()
#     print(s.lengthOfLongestSubstring("pwwkew"))
