class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while(l<r):
            m = int(l + (r-l)/2)
            
            if (m % 2 == 1 and nums[m-1] == nums[m]) or (m %2 == 0 and nums[m]== nums[m+1]):
                l = m +1
            else:
                r = m
                
        return nums[l]    
            
        