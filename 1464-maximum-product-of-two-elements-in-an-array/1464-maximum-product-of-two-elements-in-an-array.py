class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -inf
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                res = max(res,(nums[i]-1) * (nums[j]-1))
                
        return res