class Solution:
    def countPalindromes(self, s: str) -> int:
        '''
        prefix = [[0]*10 for _ in range(len(s))]
        suffix = [[0]*10 for _ in range(len(s))]
        
        prefix[0][int(s[0])] = 1
        suffix[-1][int(s[-1])] = 1

            
        for i in range(1,len(s)):
            for j in range(10):
                prefix[i][j] = prefix[i-1][j] + int(int(s[i]) == j)
        for i in range(len(s)-2,-1,-1):
            for j in range(10):
                suffix[i][j] = suffix[i+1][j] + int(int(s[i]) == j)
                
        total = 0
        MOD = 10**9 + 7
        print(prefix,suffix,)
        for i in range(2,len(s)-2):
            pals = 0
            for j in range(10):
                for k in range(10):
                    pals += min(prefix[i-1][j],suffix[i+1][j]) * min(prefix[i-2][k],suffix[i+2][k])
            total += pals
        return total % MOD
        '''
        mod, n, ans = 10 ** 9 + 7, len(s), 0
        pre, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i - 1][j][k] 
                        if k == c: pre[i][j][k] += cnts[j]
            cnts[c] += 1
        suf, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i + 1][j][k]
                        if k == c: suf[i][j][k] += cnts[j]
            cnts[c] += 1
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    ans += pre[i - 1][j][k] * suf[i + 1][j][k]
        return ans % mod
    