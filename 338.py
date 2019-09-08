class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(1, num + 1):
            ret.append(ret[i >> 1] + (i & 1))
        return ret
