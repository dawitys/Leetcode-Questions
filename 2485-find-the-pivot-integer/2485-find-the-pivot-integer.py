class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = 0
        
        for i in range(1,n+1):
            total_sum += i
        
        prefix_sum = 0
        
        for i in range(1,n+1):
            prefix_sum += i
            
            if prefix_sum == total_sum - prefix_sum + i:
                return i
        return -1