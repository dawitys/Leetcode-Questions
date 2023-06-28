class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = defaultdict(int)

        for l in s:
            best = 0
            for i in range(-k,k+1):
                best = max(best,dp[chr(ord(l)-i)])
            dp[l] = best + 1
    
        return max(dp.values())