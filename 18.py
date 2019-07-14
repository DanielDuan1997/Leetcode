class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        ret = []
        for i in range(nums_len - 3):
            if i and nums[i - 1] == nums[i]:
                continue
            sol = self.threeSum(nums, i + 1, target, nums[i])
            ret += sol
        return ret
    def threeSum(self, nums, st, target, x0):
        nums_len = len(nums)
        ret = []
        for i in range(st, nums_len):
            if i > st and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, nums_len - 1
            while True:
                while i + 1 < l and nums[l - 1] == nums[l] and l < r:
                    l += 1
                while r < nums_len - 1 and nums[r] == nums[r + 1] and l < r:
                    r -= 1
                if l >= r:
                    break
                cur_sum = x0 + nums[i] + nums[l] + nums[r]
                if cur_sum < target:
                    l += 1
                elif cur_sum == target:
                    ret.append([x0, nums[i], nums[l], nums[r]])
                    l += 1
                else:
                    r -= 1
        return ret
