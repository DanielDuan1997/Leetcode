#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
class Solution:
    def letterCombinations(self, digits: str):
        map_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        for s in digits:
            if not result:
                result = map_dict[s]
                continue
            result = [i+j for j in map_dict[s] for i in result] 
        
        result.sort()
        return result

# if __name__ == "__main__":
#     s = Solution()
#     print(s.letterCombinations('5758485'))
