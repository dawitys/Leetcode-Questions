class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        stack = []
        for i in range(n):
            
            while stack and nums[stack[-1]] <= nums[i]:
                ans[stack.pop()] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
            
        return ans