class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        for n in nums:
            if counter[n] != 3:
                return n
        