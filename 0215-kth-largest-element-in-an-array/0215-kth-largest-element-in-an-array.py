class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = [0] * 20001


        for n in nums:
            counts[n+10000] += 1
        
        pos = 0
        for i in range(len(counts)-1,-1,-1):
            pos += counts[i]
            if pos >= k:
                
                return i - 10000
            
        return -1