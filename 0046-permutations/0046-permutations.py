class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def backtrack(start):
            if start == len(nums)-1:
                output.append(nums[:])
            for i in range(start,len(nums)):
                nums[start],nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start],nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return output