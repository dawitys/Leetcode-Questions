class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        prefix = [[0,0] for _ in range(len(s))]
        suffix = [[0,0] for _ in range(len(s))]
        
        for i in range(len(s)-2,-1,-1):
            suffix[i][0] = suffix[i+1][0] + int(s[i+1]=='0')
            suffix[i][1] = suffix[i+1][1] + int(s[i+1]=='1')
            
        for i in range(1,len(s)):
            prefix[i][0] = prefix[i-1][0] + int(s[i-1]=='0')
            prefix[i][1] = prefix[i-1][1] + int(s[i-1]=='1')
    
        for i in range(1,len(s)-1):
            if s[i] == '0':
                ways += prefix[i][1]*suffix[i][1] 
            else:
                ways += prefix[i][0]*suffix[i][0] 
            
        
        
        return ways
    