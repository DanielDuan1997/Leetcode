class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float('inf')] * (amount + 1)
        f[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                f[j] = min(f[j], f[j - coin] + 1)
        if f[amount] == float('inf'):
            f[amount] = -1
        return f[amount]
