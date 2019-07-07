class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)
        ans_sum = 0
        ans_diff = 2**30
        for mid in range(nums_len):
            l, r = 0, nums_len - 1
            while l < mid < r:
                cur_sum = nums[l] + nums[mid] + nums[r]
                cur_diff = abs(target - cur_sum)
                if cur_diff < ans_diff:
                    ans_sum, ans_diff = cur_sum, cur_diff
                if cur_sum < target:
                    l += 1
                else:
                    r -= 1
        return ans_sum
