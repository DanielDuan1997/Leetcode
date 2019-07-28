class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = dict()
        for cur_str in strs:
            item = ''.join(sorted(cur_str))
            dct[item] = dct.get(item, []) + [cur_str]
        return dct.values()
