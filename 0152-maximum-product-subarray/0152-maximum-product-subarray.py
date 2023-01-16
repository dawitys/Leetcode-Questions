class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_multiple = min_multiple = nums[0]
        
        for i in range(1,len(nums)):
            max_multiple, min_multiple = max(nums[i], max_multiple*nums[i],min_multiple*nums[i]) \
                ,min(nums[i], max_multiple*nums[i],min_multiple*nums[i])
            
            ans = max(ans, max_multiple)
        
        return ans