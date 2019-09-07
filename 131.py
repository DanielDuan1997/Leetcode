class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        is_palindrome = [False for i in range(len(s))]
        f = [[] for i in range(len(s))]
        for i in range(len(s)):
            if i > 0:
                f[i] = [item + [s[i]] for item in f[i-1]]
            else:
                f[i] = [[s[0]]]
            is_palindrome[i] = True
            for j in range(i):
                if s[j] == s[i] and is_palindrome[j + 1]:
                    cur_str = s[j:i+1]
                    if j > 0:
                        f[i] += [item + [cur_str] for item in f[j - 1]]
                    else:
                        f[i] += [[cur_str]]
                    is_palindrome[j] = True
                else:
                    is_palindrome[j] = False
        return f[len(s) - 1]
