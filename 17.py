class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dct = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ret = []
        def dfs(comb, digits, left):
            if left == 0:
                ret.append(comb)
            else:
                for ch in dct.get(digits[0]):
                    dfs(comb + ch, digits[1:], left - 1)
        dfs("", digits, len(digits))
        return ret
