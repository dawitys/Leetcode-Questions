class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(nums, i, j):
            rob, not_rob = 0, 0
            for idx in range(i, j):
                num = nums[idx]
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(simple_rob(nums, 1, n), simple_rob(nums, 0, n-1))