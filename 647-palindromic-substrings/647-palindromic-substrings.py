class Solution:
    def countSubstrings(self, s: str) -> int:
        palindroms = 0
        for i in range(len(s)):
            palindroms += 1
            l,r = i-1,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                palindroms += 1
                l -=1
                r +=1
        
        
        for i in range(len(s)):
            l,r = i,i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                palindroms += 1
                l -=1
                r +=1
                
                
        return palindroms