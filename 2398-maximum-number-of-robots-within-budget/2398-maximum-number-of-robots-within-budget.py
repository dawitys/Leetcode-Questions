from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        left = 0
        res = 0
        # strictly decreasing for chargeTime, and queue[0] is the largest chargeTime
        queue = deque()
        sum_cost = 0
        
        for i in range(len(chargeTimes)):
            
            # in
            sum_cost += runningCosts[i]
            
            # keep the largest chargeTime
            while queue and chargeTimes[queue[-1]] <= chargeTimes[i]:
                queue.pop()
            
            queue.append(i)
            
            # out
            while queue and chargeTimes[queue[0]] + (i - left + 1) * sum_cost > budget:
                
                if queue and queue[0] == left:
                    queue.popleft()
                
                sum_cost -= runningCosts[left]
                
                left += 1
            # compute
            res = max(res, i - left + 1)
        
        return res