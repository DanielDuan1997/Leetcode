class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        LISLen = 0
        for i in range(n):
            if LISLen == 0 or nums[i] > f[LISLen]:
                LISLen += 1
                f[LISLen] = nums[i]
            else:
                le, ri = 1, LISLen
                while le <= ri:
                    mi = (le + ri) // 2
                    if f[mi] < nums[i]:
                        le = mi + 1
                    else:
                        ri = mi - 1
                f[le] = nums[i]
        return LISLen
