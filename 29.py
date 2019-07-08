class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        dividend_init = dividend
        divisor = abs(divisor)
        ans = 0
        for i in range(32, -1 ,-1):
            x = divisor << i
            if dividend >= x:
                dividend -= x
                ans += 1 << i
            if dividend == 0:
                break
        if neg:
            ans = -ans
        ans = min(ans, 2**31 - 1)
        return ans
