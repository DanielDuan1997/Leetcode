class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def dfs(cur_str, n, pre_sum):
            if n == 0 and pre_sum == 0:
                ret.append(cur_str)
                return
            if n:
                dfs(cur_str + '(', n - 1, pre_sum + 1)
            if pre_sum:
                dfs(cur_str + ')', n, pre_sum - 1)
        dfs("", n, 0)
        return ret
