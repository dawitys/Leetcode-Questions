class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        
        curr = 0
        count = 0
        for i in range(len(nums)):
            curr += nums[i]
            curr %= k
            if curr in seen:
                count += seen[curr]
            seen[curr] += 1
            
            
        return count