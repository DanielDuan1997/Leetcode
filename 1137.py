class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [0, 1, 1]
        if n < 3:
            return ret[n]
        for i in range(3, n + 1):
            ret.append(ret[-3] + ret[-2] + ret[-1])
        return ret[-1]
