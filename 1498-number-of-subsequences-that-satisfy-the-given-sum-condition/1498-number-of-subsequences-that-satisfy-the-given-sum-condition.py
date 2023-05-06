class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        nums.sort()
        
        res = 0
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += 2 ** (right - left)
                left += 1
                
        return res % MOD
            
            