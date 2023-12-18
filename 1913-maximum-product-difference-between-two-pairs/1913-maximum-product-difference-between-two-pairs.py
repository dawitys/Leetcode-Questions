class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')
        for num in nums:
            if num < min1:
                min1,min2 = num,min1 
            elif num < min2:
                min2 = num 
            
            if num > max1:
                max1,max2 = num,max1 
            elif num > max2:
                max2 = num 
                
        return (max2*max1) - (min2*min1)
