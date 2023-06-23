class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        
        to_remove = len(nums) - k
        for i,n in enumerate(nums):
            while stack and stack[-1] > n and to_remove:
                stack.pop()
                to_remove -= 1
            stack.append(n)
            
        return stack[:-to_remove] if to_remove else stack
                