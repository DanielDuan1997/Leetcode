#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for idx, i in enumerate(nums):
            if idx > 0:
                if nums[idx] == nums[idx - 1]:
                    continue
            s = -i
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < s:
                    left += 1
                elif nums[left] + nums[right] > s:
                    right -= 1
                else:
                    result.append([i, nums[left], nums[right]])
                    left += 1
                    while left > 1 and left < right and nums[left] == nums[
                            left - 1]:
                        left += 1

        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.threeSum([0,0,0,0]))
