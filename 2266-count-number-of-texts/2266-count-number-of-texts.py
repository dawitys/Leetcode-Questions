class Solution:
    def countTexts(self, A: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * (len(A)+1)
        dp[0] = 1
        for i in range(1,len(A)+1):
            dp[i] = dp[i-1]
            if i>1 and A[i-1] == A[i-2]:
                dp[i] += dp[i-2]

                if i>2 and A[i-1] == A[i-3]:
                    dp[i] += dp[i-3]

                    if A[i-1] in '97' and i>3 and A[i-1] == A[i-4]:
                        dp[i] += dp[i-4]

        return dp[-1] % MOD