class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        flag = False
        for i in range(len_nums - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                flag = True
                break
        if not flag:
            nums = nums.reverse()
        else:
            for j in range(len_nums - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i + 1:] = nums[i + 1:][::-1]
