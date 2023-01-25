class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 0
        
        for i in range( (total//cost1)+1):
            pencil_ways = ((total - i*cost1)//cost2) + 1
            ways += pencil_ways
        return ways