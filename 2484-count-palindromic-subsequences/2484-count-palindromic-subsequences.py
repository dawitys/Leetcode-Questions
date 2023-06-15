class Solution:
    def countPalindromes(self, s: str) -> int:
       
        n = len(s)
        prefix = [[[0]*10 for _ in range(10)] for _ in range(n)]
        suffix = [[[0]*10 for _ in range(10)] for _ in range(n)]

        counts = [0]*10
        for i in range(n):
            if i:
                for j in range(10):
                    for k in range(10):
                        prefix[i][j][k] = prefix[i-1][j][k]
                        if int(s[i]) == k:
                            prefix[i][j][k] += counts[j]
                        
            counts[int(s[i])] += 1
        
        counts = [0]*10          
        for i in range(n-1,-1,-1):
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suffix[i][j][k] = suffix[i+1][j][k] 
                        if int(s[i]) == k:
                            suffix[i][j][k] += counts[j]

            counts[int(s[i])] += 1
        total = 0
        MOD = 10**9 + 7

        for i in range(2,n-2):
            for j in range(10):
                for k in range(10):
                    total += prefix[i-1][j][k]*suffix[i+1][j][k]

        return total % MOD