class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            for curr in range(1,amount+1):
                if curr >= c:
                    dp[curr] += dp[curr-c]

        return dp[amount]