class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len < 3:
            return []
        nums.sort()
        ret = []
        for mid in range(nums_len):
            if mid and nums[mid - 1] == nums[mid]:
                if mid > 1 and nums[mid - 2] == nums[mid]: continue
                for r in range(mid + 1, nums_len):
                    if 2 * nums[mid] + nums[r] == 0:
                        ret.append([nums[mid], nums[mid], nums[r]])
                        break
                continue
            l, r = 0, nums_len - 1
            while True:
                while 0 < l < mid and nums[l - 1] == nums[l]: l += 1
                while mid < r <  nums_len - 1 and nums[r] == nums[r + 1]: r -= 1
                if not (l < mid < r):
                    break
                cur_sum = nums[l] + nums[mid] + nums[r]
                if cur_sum < 0:
                    l += 1
                elif cur_sum == 0:
                    ret.append([nums[l], nums[mid], nums[r]])
                    l += 1
                    r -= 1
                else:
                    r -= 1
        return ret
