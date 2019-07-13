#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2^31 - 1
        MIN_INT = -2^31
        
        result = dividend / divisor
        
        if result > MAX_INT:
            return MAX_INT
        elif result < MIN_INT:
            return MIN_INT
        else:
            return result

