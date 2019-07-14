#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        neg = (dividend > 0) != (divisor > 0)
        if dividend < 0:
            dividend = ~dividend + 1
        if divisor < 0:
            divisor = ~divisor + 1
        temp_divisor = divisor
        quotient = 0
        if dividend - divisor >= 0:
            temp_quotient = 1
            while True:
                if dividend - divisor < 0:
                    break
                if dividend - (temp_divisor << 1) >= 0:
                    temp_quotient = temp_quotient << 1
                    temp_divisor = temp_divisor << 1

                elif dividend - temp_divisor >=0:
                    dividend -= temp_divisor
                    quotient += temp_quotient
                    temp_quotient = temp_quotient >> 1
                    temp_divisor = temp_divisor >> 1
                else:
                    temp_quotient = temp_quotient >> 1
                    temp_divisor = temp_divisor >> 1

            # divisor < dividend < 2*divisor
        if neg:
            quotient = ~quotient + 1
        if quotient > MAX_INT:
            return MAX_INT
        elif quotient < MIN_INT:
            return MIN_INT
        else:
            return quotient


if __name__ == "__main__":
    s = Solution()
    print(s.divide(7, 3))
