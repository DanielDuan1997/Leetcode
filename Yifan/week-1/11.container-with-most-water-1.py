#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (42.45%)
# Likes:    3458
# Dislikes: 453
# Total Accepted:    395.2K
# Total Submissions: 872.8K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49.
#
#
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#
#
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        max_height = min(height)
        min_height = min(height)

        n = len(height)
        if height.index(max(height))>n/2:
            height.reverse()

        for i, h in enumerate(height):
            if h<min_height:
                continue
            elif i>0 and h<height[i-1]:
                continue
            for j in range(n-i):
                area = min(h,height[j+i]) * j
                if area > max_area:
                    max_area = area
                    min_height = min(h,height[j+i])
        return max_area


# if __name__ == "__main__":
#     s = Solution()
#     print(s.maxArea([1,2,3,4,5,6]))
