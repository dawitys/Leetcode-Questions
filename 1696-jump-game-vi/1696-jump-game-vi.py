from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = []
        best = 0
        for i in range(len(nums)):
            maxV = 0
            if queue:
                maxV, idx = queue[0]
                while idx + k < i:
                    maxV, idx = heapq.heappop(queue)
                    
                heapq.heappush(queue, [maxV,idx])
                
            best = nums[i] + (-1) * maxV
            heapq.heappush(queue, [-1 * best, i]) 
            
        return best