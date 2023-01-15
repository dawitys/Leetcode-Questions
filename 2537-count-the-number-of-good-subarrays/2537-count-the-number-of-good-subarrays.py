class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        pairs = good_count = 0

        l = r = 0
        while l <= r and r < len(nums):
            pairs += frequency[nums[r]]
            frequency[nums[r]] += 1
            
            while pairs >= k:
                good_count += len(nums) - r
                frequency[nums[l]] -= 1
                pairs -= frequency[nums[l]]
                l += 1          
            r += 1
            
        return good_count
