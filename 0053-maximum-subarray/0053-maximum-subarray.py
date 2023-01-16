class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = 0
        ans = -inf
        for n in nums:
            best = max(best+n, n)
            ans = max(best,ans)

        
        return ans