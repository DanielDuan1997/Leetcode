class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        len_candidates = len(candidates)
        def dfs(target, candidates, pos, lst):
            if target == 0:
                ret.append(lst)
                return
            if pos == len_candidates:
                return
            if candidates[pos] <= target:
                dfs(target - candidates[pos], candidates, pos, lst + [candidates[pos]])
            dfs(target, candidates, pos + 1, lst)
        dfs(target, candidates, 0, [])
        return ret
