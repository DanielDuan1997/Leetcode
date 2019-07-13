#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        min = 1000000
        mt = 0
        for idx, i in enumerate(nums):
            if idx >0:
                if nums[idx]==nums[idx-1]:
                    continue

            s = target-i
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                dis = abs(nums[left] + nums[right]-s)
                if dis <= min:
                    min = dis
                    mt = nums[left] + nums[right]+i
                if nums[left] + nums[right] < s:
                    left += 1
                elif nums[left] + nums[right] > s:
                    right -= 1
                else:
                    return target
        return mt



if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1,1,1,1],-100))
