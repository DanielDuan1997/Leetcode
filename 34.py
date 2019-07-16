class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        if len_nums == 0:
            return [-1, -1]
        def lower_bound(le, ri):
            while le <= ri:
                mid = (le + ri) // 2
                if target <= nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            return ri + 1
        def upper_bound(le, ri):
            while le <= ri:
                mid = (le + ri) // 2
                if target < nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            return le - 1
        ans_l = lower_bound(0, len_nums - 1)
        if ans_l == len_nums or nums[ans_l] != target:
            return [-1, -1]
        else:
            return [ans_l, upper_bound(ans_l, len_nums - 1)]
