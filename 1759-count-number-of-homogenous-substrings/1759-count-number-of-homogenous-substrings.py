class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        
        last,count = '',0
        subs = 0

        l = r = 0
        while l <= r and r < len(s):
            if s[r] == last:
                count += 1
                subs += count
                r += 1
            else:
                subs += 1
                last = s[r]
                count = 1
                l = r = r+1
            
        return subs % MOD
