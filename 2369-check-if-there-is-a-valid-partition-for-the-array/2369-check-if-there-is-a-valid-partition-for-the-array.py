class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                dp[i+1] |= dp[i-1]
            
            if i > 1 and nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                dp[i+1] |= dp[i-2]
            
            if i > 1 and nums[i]-1 == nums[i-1] and nums[i-1]-1 == nums[i-2]:
                dp[i+1] |= dp[i-2]
        
        return dp[-1]