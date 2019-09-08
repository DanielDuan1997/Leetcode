class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        for i in range(n):
            if i == 0:
                if nums[0] > nums[1]:
                    return 0
            elif i == n-1:
                if nums[n-1] > nums[n-2]:
                    return n-1
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
