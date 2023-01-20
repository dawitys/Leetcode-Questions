class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        changes = defaultdict(int)
        
        for original, new in operations:
            if original in changes:
                changes[new] = changes[original]
                del changes[original]
            else:
                changes[new] = original
        
        pair = {}
        for new,old in changes.items():
            pair[old] = new
        
        for i in range(len(nums)):
            if nums[i] in pair:
                nums[i] = pair[nums[i]]
        
        return nums