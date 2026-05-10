class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # Base case: 0 coins to make amount 0

        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    dp[target] = min(dp[target], 1 + dp[target - coin])

        return dp[amount] if dp[amount] != float('inf') else -1
        