class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_one = -1
        last_two = len(nums) - 1
        cur_pos = 0
        while cur_pos <= last_two:
            if nums[cur_pos] == 0:
                if first_one != -1:
                    nums[cur_pos], nums[first_one] = nums[first_one], nums[cur_pos]
                    first_one += 1
                cur_pos += 1
            elif nums[cur_pos] == 1:
                if first_one == -1:
                    first_one = cur_pos
                cur_pos += 1
            else:
                while cur_pos < last_two and nums[last_two] == 2:
                    last_two -= 1
                if cur_pos == last_two:
                    break
                else:
                    nums[cur_pos], nums[last_two] = nums[last_two], nums[cur_pos]
