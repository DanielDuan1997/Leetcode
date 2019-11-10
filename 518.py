class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f =  [0] * (amount + 1)
        f[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                f[j] += f[j - coin]
        return f[amount]
