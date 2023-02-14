class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefixB = [0] * len(s)
        suffixA = [0] * len(s)
        
        for i in range(1,len(s)):
            prefixB[i] = prefixB[i-1] + int(s[i-1]=='b') 
        
        for i in range(len(s)-2,-1,-1):
            suffixA[i] = suffixA[i+1] + int(s[i+1] == 'a')
        
        min_del = inf
        
        for i in range(len(s)):
            min_del = min(min_del,prefixB[i]+suffixA[i])
        
        return min_del