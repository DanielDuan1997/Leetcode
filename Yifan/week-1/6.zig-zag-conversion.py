#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s

        result=[]
        thr = len(s)
        n = 2*numRows-2
        for i in range(numRows):
            p = [j for j in range(i,thr,n)]
            if i >0 and 2*i!=n:
                m = [j for j in range(n-i,thr,n)]
                p.extend(m)
                p.sort()
            result.extend([s[j] for j in p])
        return ''.join(result)

if __name__ == "__main__":
    s = Solution()
    print(s.convert('adhalajdl',1))
