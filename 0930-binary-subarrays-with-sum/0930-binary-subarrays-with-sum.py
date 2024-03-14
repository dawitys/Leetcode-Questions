class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:    
        
        def atMost(g):
            count = running_sum = l = 0
            for r in range(len(nums)):
                running_sum += nums[r]
                while l<=r and running_sum > g:
                    running_sum -= nums[l]
                    l += 1
                count += r-l+ 1
            return count
        return atMost(goal) - atMost(goal-1)