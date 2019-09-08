class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        shift = 0
        while m and m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift
