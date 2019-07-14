#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) == 4:
            if sum(nums)==target:
                return [nums]
            else:
                return []
        result = []
        for idx, i in enumerate(nums):
            if idx > len(nums) - 4:
                break
            if idx > 0 and i == nums[idx - 1]:
                continue
            for jdx, j in enumerate(nums[idx + 1:]):
                jdx = idx + 1 + jdx
                if jdx > len(nums) - 3:
                    break
                if jdx > idx + 1 and j == nums[jdx - 1]:
                    continue
                left = jdx + 1
                right = len(nums) - 1
                while left < right:
                    tar_sum = nums[left] + nums[right] + j + i - target
                    if tar_sum == 0:
                        result.append([i, j, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif tar_sum > 0:
                        right -= 1
                    elif tar_sum < 0:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result


if __name__ == "__main__":
    print(Solution().fourSum([-1,-5,-5,-3,2,5,0,4], -7))
