class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp=[0,1]
        for i in range(2,n + 1):
            dp += [dp[i//2] if i % 2==0 else dp[i//2] + dp[i//2 + 1]]
        return max(dp[:n + 1])