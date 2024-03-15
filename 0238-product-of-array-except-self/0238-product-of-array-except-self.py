class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        pre = 1
        
        for i in range(1,len(nums)):
            pre *= nums[i-1]
            ans[i] *= pre 
            
        pre = 1
        for i in range(len(nums)-2,-1,-1):
            pre *= nums[i+1]
            ans[i] *= pre 
            
        return ans