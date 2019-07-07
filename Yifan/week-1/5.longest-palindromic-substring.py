#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        result = s[0]
        for i in range(len(s)):
            idx = s[i:].rfind(s[i]) 
            while idx>=0:
                temp = s[i:i+idx+1] #注意末位
                if temp!=temp[::-1]:
                    idx = s[i:i+idx].rfind(s[i]) #缩小范围
                else:
                    break
            if idx>=0 and len(temp)>len(result):
                result = temp
        return result
                
# if __name__ == "__main__":
#     s=Solution()
#     a =s.longestPalindrome("abcdbbfcba")
#     print(a)
