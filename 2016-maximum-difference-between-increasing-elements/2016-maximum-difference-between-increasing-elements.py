class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, nums[j]-nums[i])
                    
        return ans