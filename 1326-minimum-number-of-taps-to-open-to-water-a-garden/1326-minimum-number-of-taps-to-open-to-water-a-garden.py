class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 1] * n
        for i, r in enumerate(ranges):
            for j in range(max(i - r, 0), min(i + r, n)):
                dp[j + 1] = min(dp[j + 1], dp[max(0, i - r)] + 1)
        return dp[n] if dp[n] < n + 1 else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        mini  = maxi  = opens  = 0
        idx = 0
        while maxi<n:
            for i in range(idx,len(ranges)):
                if i-ranges[i]<=mini and i+ranges[i]>maxi:
                    maxi=i+ranges[i]
                    idx=i
            if mini==maxi:
                return -1
            opens+=1
            mini = maxi
        return opens        
        '''
