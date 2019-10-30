class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        tmp = []
        n = len(nums)
        big_ind = n - 1
        mid = n // 2 - (0 if n & 1 else 1)
        for i in range(mid, -1, -1):
            tmp.append(nums[i])
            if big_ind > mid:
                tmp.append(nums[big_ind])
                big_ind -= 1
        for i in range(n):
            nums[i] = tmp[i]
