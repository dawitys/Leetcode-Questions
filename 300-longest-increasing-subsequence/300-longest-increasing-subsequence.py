class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # a =  6
        # arr = [1,2,3,4,5,6,6,6,6,6,7]        
        # return bisect.bisect_right(arr,a)
        
        # 
        
        ans = 1
        dp = []
        
        for n in nums:
            pos =bisect.bisect_left(dp,n)
            if pos == len(dp):
                dp.append(n)
            else:
                dp[pos] = n
        return len(dp)
        
