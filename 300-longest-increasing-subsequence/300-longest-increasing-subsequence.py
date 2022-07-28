class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # a =  6
        # arr = [1,2,3,4,5,6,6,6,6,6,7]        
        # return bisect.bisect_right(arr,a)
        
        ans = 1
        dp = [1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            maxpossible = 1
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    maxpossible = max(maxpossible,dp[j]+1)
            
            
            dp[i] = maxpossible
            
        # print(dp)
        return max(dp)
        
